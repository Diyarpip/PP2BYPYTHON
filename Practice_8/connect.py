import psycopg2
from config import config

def connect():
    conn = None
    try:
        params = config()
        print('Connecting to PostgreSQL...')
        conn = psycopg2.connect(**params)
        
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook2 (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                phone VARCHAR(20) NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cur.execute("""
            CREATE OR REPLACE FUNCTION search_by_pattern(p_pattern TEXT)
            RETURNS TABLE(
                id INT,
                name VARCHAR(100),
                phone VARCHAR(20),
                created_at TIMESTAMP
            ) AS $$
            BEGIN
                RETURN QUERY
                SELECT phonebook2.id, phonebook2.name, phonebook2.phone, phonebook2.created_at
                FROM phonebook2
                WHERE phonebook2.name ILIKE '%' || p_pattern || '%'
                   OR phonebook2.phone ILIKE '%' || p_pattern || '%'
                ORDER BY phonebook2.name;
            END;
            $$ LANGUAGE plpgsql;
        """)
        
        cur.execute("""
            CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
            RETURNS TABLE(
                id INT,
                name VARCHAR(100),
                phone VARCHAR(20),
                created_at TIMESTAMP
            ) AS $$
            BEGIN
                RETURN QUERY
                SELECT phonebook2.id, phonebook2.name, phonebook2.phone, phonebook2.created_at
                FROM phonebook2
                ORDER BY phonebook2.name
                LIMIT p_limit OFFSET p_offset;
            END;
            $$ LANGUAGE plpgsql;
        """)
        
        cur.execute("""
            CREATE OR REPLACE PROCEDURE upsert_contact(
                p_name VARCHAR(100),
                p_phone VARCHAR(20)
            )
            LANGUAGE plpgsql AS $$
            BEGIN
                INSERT INTO phonebook2 (name, phone) 
                VALUES (p_name, p_phone)
                ON CONFLICT (phone) 
                DO UPDATE SET 
                    name = EXCLUDED.name,
                    created_at = CURRENT_TIMESTAMP;
            END;
            $$;
        """)
        
        cur.execute("""
            CREATE OR REPLACE PROCEDURE insert_validated_contacts(
                p_names TEXT[],
                p_phones TEXT[]
            )
            LANGUAGE plpgsql AS $$
            DECLARE
                i INT;
                v_phone_pattern TEXT := '^\\+7[0-9]{10}$|^8[0-9]{10}$|^[0-9]{10}$';
            BEGIN
                FOR i IN 1..array_length(p_names, 1) LOOP
                    IF p_phones[i] ~ v_phone_pattern THEN
                        IF p_phones[i] ~ '^8[0-9]{10}$' THEN
                            p_phones[i] := '+7' || substring(p_phones[i] FROM 2);
                        ELSIF p_phones[i] ~ '^[0-9]{10}$' THEN
                            p_phones[i] := '+7' || p_phones[i];
                        END IF;
                        
                        INSERT INTO phonebook2 (name, phone) 
                        VALUES (p_names[i], p_phones[i])
                        ON CONFLICT (phone) DO UPDATE 
                        SET name = EXCLUDED.name;
                    END IF;
                END LOOP;
            END;
            $$;
        """)
        
        cur.execute("""
            CREATE OR REPLACE PROCEDURE delete_by_name_or_phone(p_search_term TEXT)
            LANGUAGE plpgsql AS $$
            BEGIN
                DELETE FROM phonebook2
                WHERE name ILIKE '%' || p_search_term || '%'
                   OR phone = p_search_term;
            END;
            $$;
        """)
        
        cur.execute("""
            CREATE OR REPLACE FUNCTION get_phonebook_stats()
            RETURNS TABLE(
                total_contacts BIGINT,
                last_created TIMESTAMP,
                phone_patterns JSON
            ) AS $$
            BEGIN
                RETURN QUERY
                SELECT 
                    COUNT(*)::BIGINT as total_contacts,
                    MAX(created_at) as last_created,
                    json_build_object(
                        'start_with_plus7', COUNT(*) FILTER (WHERE phone LIKE '+7%'),
                        'start_with_8', COUNT(*) FILTER (WHERE phone LIKE '8%'),
                        'other', COUNT(*) FILTER (WHERE phone NOT LIKE '+7%' AND phone NOT LIKE '8%')
                    ) as phone_patterns
                FROM phonebook2;
            END;
            $$ LANGUAGE plpgsql;
        """)
        
        conn.commit()
        print('Table and functions ready')
        return conn, cur
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f'Error: {error}')
        return None, None