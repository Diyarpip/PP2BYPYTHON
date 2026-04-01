import csv
import sys
from connect import connect

class PhoneBook:
    def __init__(self):
        self.conn, self.cur = connect()
        if not self.conn:
            print("Не удалось подключиться к базе данных")
            sys.exit(1)
    
    def add_contact(self, name, phone):
        try:
            self.cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s) RETURNING id",
                (name, phone)
            )
            self.conn.commit()
            print(f"✅ Контакт '{name}' успешно добавлен!")
            return True
        except Exception as e:
            print(f"❌ Ошибка при добавлении: {e}")
            self.conn.rollback()
            return False
    
    def search_contacts(self, search_term):
        self.cur.execute(
            "SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s",
            (f'%{search_term}%', f'%{search_term}%')
        )
        return self.cur.fetchall()
    
    def list_all_contacts(self):
        self.cur.execute("SELECT * FROM phonebook ORDER BY name")
        return self.cur.fetchall()
    
    def update_contact(self, contact_id, name=None, phone=None):
        updates = []
        values = []
        
        if name:
            updates.append("name = %s")
            values.append(name)
        if phone:
            updates.append("phone = %s")
            values.append(phone)
        
        if not updates:
            return False
        
        values.append(contact_id)
        query = f"UPDATE phonebook SET {', '.join(updates)} WHERE id = %s"
        
        try:
            self.cur.execute(query, values)
            self.conn.commit()
            print(f"✅ Контакт {contact_id} обновлен!")
            return True
        except Exception as e:
            print(f"❌ Ошибка при обновлении: {e}")
            self.conn.rollback()
            return False
    
    def delete_contact(self, contact_id):
        try:
            self.cur.execute("DELETE FROM phonebook WHERE id = %s", (contact_id,))
            self.conn.commit()
            print(f"✅ Контакт {contact_id} удален!")
            return True
        except Exception as e:
            print(f"❌ Ошибка при удалении: {e}")
            self.conn.rollback()
            return False
    
    def import_from_csv(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Пропускаем заголовок
                
                for row in csv_reader:
                    if len(row) >= 2:
                        name, phone = row[0], row[1]
                        self.add_contact(name, phone)
            
            print(f"✅ Импорт из {filename} завершен!")
            return True
        except Exception as e:
            print(f"❌ Ошибка при импорте: {e}")
            return False
    
    def display_contacts(self, contacts):
        if not contacts:
            print("📭 Контакты не найдены")
            return
        
        print("\n" + "="*60)
        print(f"{'ID':<5} {'Имя':<30} {'Телефон':<20}")
        print("="*60)
        
        for contact in contacts:
            print(f"{contact[0]:<5} {contact[1]:<30} {contact[2]:<20}")
        print("="*60)
    
    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("🔌 Соединение закрыто")

def main():
    pb = PhoneBook()
    
    while True:
        print("\n📞 === PHONEBOOK MENU ===")
        print("1. ➕ Добавить контакт")
        print("2. 🔍 Поиск контакта")
        print("3. 📋 Показать все контакты")
        print("4. ✏️ Обновить контакт")
        print("5. 🗑️ Удалить контакт")
        print("6. 📥 Импорт из CSV")
        print("7. 🚪 Выход")
        
        choice = input("\nВыберите действие (1-7): ")
        
        if choice == '1':
            name = input("Имя: ")
            phone = input("Телефон: ")
            pb.add_contact(name, phone)
        
        elif choice == '2':
            search = input("Введите имя или телефон для поиска: ")
            results = pb.search_contacts(search)
            pb.display_contacts(results)
        
        elif choice == '3':
            contacts = pb.list_all_contacts()
            pb.display_contacts(contacts)
        
        elif choice == '4':
            contact_id = input("ID контакта для обновления: ")
            print("Оставьте поле пустым, если не хотите менять")
            name = input("Новое имя: ")
            phone = input("Новый телефон: ")
            pb.update_contact(
                int(contact_id),
                name if name else None,
                phone if phone else None
            )
        
        elif choice == '5':
            contact_id = input("ID контакта для удаления: ")
            pb.delete_contact(int(contact_id))
        
        elif choice == '6':
            filename = input("Имя CSV файла (например, contacts.csv): ")
            pb.import_from_csv(filename)
        
        elif choice == '7':
            pb.close()
            print("👋 До свидания!")
            break
        
        else:
            print("❌ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()