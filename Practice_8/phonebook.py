# phonebook.py
import csv
import sys
from connect import connect

class PhoneBookV2:
    def __init__(self):
        self.conn, self.cur = connect()
        if not self.conn:
            print("Не удалось подключиться")
            sys.exit(1)
    
    def add_or_update_contact(self, name, phone):
        try:
            self.cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
            self.conn.commit()
            print(f"Контакт {name} успешно добавлен или обновлен")
            return True
        except Exception as e:
            print(f"Ошибка: {e}")
            self.conn.rollback()
            return False
    
    def search_contacts(self, search_term):
        try:
            self.cur.execute("SELECT * FROM search_by_pattern(%s)", (search_term,))
            return self.cur.fetchall()
        except Exception as e:
            print(f"Ошибка: {e}")
            return []
    
    def get_paginated_contacts(self, limit, offset):
        try:
            self.cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
            return self.cur.fetchall()
        except Exception as e:
            print(f"Ошибка: {e}")
            return []
    
    def list_all_contacts(self):
        try:
            self.cur.execute("SELECT * FROM phonebook2 ORDER BY name")
            return self.cur.fetchall()
        except Exception as e:
            print(f"Ошибка: {e}")
            return []
    
    def delete_contacts_by_pattern(self, search_term):
        try:
            self.cur.execute("CALL delete_by_name_or_phone(%s)", (search_term,))
            self.conn.commit()
            print("Контакты успешно удалены")
            return True
        except Exception as e:
            print(f"Ошибка: {e}")
            self.conn.rollback()
            return False
    
    def import_with_validation(self, filename):
        try:
            names = []
            phones = []
            
            with open(filename, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                
                for row in csv_reader:
                    if len(row) >= 2:
                        names.append(row[0])
                        phones.append(row[1])
            
            if names:
                self.cur.execute("CALL insert_validated_contacts(%s, %s)", (names, phones))
                self.conn.commit()
                print(f"Импорт из {filename} завершен")
                return True
            else:
                print("Нет данных")
                return False
                
        except Exception as e:
            print(f"Ошибка: {e}")
            self.conn.rollback()
            return False
    
    def get_statistics(self):
        try:
            self.cur.execute("SELECT * FROM get_phonebook_stats()")
            result = self.cur.fetchone()
            if result:
                print("\n=== СТАТИСТИКА ===")
                print(f"Всего контактов: {result[0]}")
                print(f"Последнее обновление: {result[1]}")
                print(f"Статистика по телефонам: {result[2]}")
            return result
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
    
    def display_contacts(self, contacts, title="Контакты"):
        if not contacts:
            print("Контакты не найдены")
            return
        
        print(f"\n{title}")
        print("=" * 80)
        print(f"{'ID':<5} {'Имя':<30} {'Телефон':<20} {'Создан':<20}")
        print("=" * 80)
        
        for contact in contacts:
            created_at = contact[3].strftime("%Y-%m-%d %H:%M") if len(contact) > 3 else "N/A"
            print(f"{contact[0]:<5} {contact[1]:<30} {contact[2]:<20} {created_at:<20}")
        print("=" * 80)
        print(f"Всего: {len(contacts)} контактов")
    
    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("Соединение закрыто")

def main():
    pb = PhoneBookV2()
    
    while True:
        print("\nМЕНЮ PHONEBOOK V2")
        print("1. Добавить или обновить контакт")
        print("2. Поиск контактов")
        print("3. Показать все контакты")
        print("4. Пагинация")
        print("5. Удалить по имени или телефону")
        print("6. Импорт с валидацией")
        print("7. Статистика")
        print("8. Выход")
        
        choice = input("Выберите действие (1-8): ")
        
        if choice == '1':
            name = input("Имя: ")
            phone = input("Телефон: ")
            pb.add_or_update_contact(name, phone)
        
        elif choice == '2':
            search = input("Введите имя или телефон: ")
            results = pb.search_contacts(search)
            pb.display_contacts(results, "Результаты поиска")
        
        elif choice == '3':
            contacts = pb.list_all_contacts()
            pb.display_contacts(contacts, "Все контакты")
        
        elif choice == '4':
            try:
                limit = int(input("Записей на странице: "))
                offset = int(input("Пропустить записей: "))
                contacts = pb.get_paginated_contacts(limit, offset)
                pb.display_contacts(contacts, f"Пагинация (limit={limit}, offset={offset})")
            except ValueError:
                print("Введите целые числа!")
        
        elif choice == '5':
            search = input("Введите имя или телефон для удаления: ")
            confirm = input(f"Удалить все содержащие '{search}'? (y/n): ")
            if confirm.lower() == 'y':
                pb.delete_contacts_by_pattern(search)
        
        elif choice == '6':
            filename = input("Имя CSV файла: ")
            pb.import_with_validation(filename)
        
        elif choice == '7':
            pb.get_statistics()
        
        elif choice == '8':
            pb.close()
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()