import psycopg2
from config import config

def connect():
    conn = None
    try:
        params = config()
        print('Подключение к PostgreSQL...')
        conn = psycopg2.connect(**params)
        
        cur = conn.cursor()
        
        # Создаем таблицу без email
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                phone VARCHAR(20) NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        print('✅ Таблица phonebook готова')
        return conn, cur
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f'❌ Ошибка: {error}')
        return None, None