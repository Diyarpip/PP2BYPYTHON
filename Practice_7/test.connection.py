from connect import connect

def test_connection():
    conn, cur = connect()
    if conn:
        print("✅ Подключение к базе данных успешно!")
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print(f"PostgreSQL версия: {version[0]}")
        
        # Проверяем структуру таблицы
        cur.execute("""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = 'phonebook'
        """)
        columns = cur.fetchall()
        print("\nСтруктура таблицы phonebook:")
        for col in columns:
            print(f"  - {col[0]}: {col[1]}")
        
        cur.close()
        conn.close()
    else:
        print("❌ Не удалось подключиться к базе данных")

if __name__ == "__main__":
    test_connection()