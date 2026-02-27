import json

def main():
    # Читаем две строки
    str1 = input().strip()
    str2 = input().strip()
    
    # Превращаем JSON в объекты
    obj1 = json.loads(str1)
    obj2 = json.loads(str2)
    
    # Находим различия
    result = []
    find_diffs(obj1, obj2, "", result)
    
    # Сортируем по пути
    result.sort(key=lambda x: x[0])
    
    # Выводим
    if not result:
        print("No differences")
    else:
        for path, old, new in result:
            print(f"{path} : {old} -> {new}")

def find_diffs(val1, val2, path, result):
    # Проверяем типы
    if type(val1) != type(val2):
        result.append((path, json.dumps(val1), json.dumps(val2)))
        return
    
    # Для словарей
    if isinstance(val1, dict):
        # Все ключи из первого словаря
        for key in val1:
            new_path = path + "." + key if path else key
            if key not in val2:
                result.append((new_path, json.dumps(val1[key]), "<missing>"))
            else:
                find_diffs(val1[key], val2[key], new_path, result)
        
        # Ключи, которые есть только во втором словаре
        for key in val2:
            if key not in val1:
                new_path = path + "." + key if path else key
                result.append((new_path, "<missing>", json.dumps(val2[key])))
        return
    
    # Для списков
    if isinstance(val1, list):
        max_len = max(len(val1), len(val2))
        for i in range(max_len):
            new_path = path + "." + str(i) if path else str(i)
            if i >= len(val1):
                result.append((new_path, "<missing>", json.dumps(val2[i])))
            elif i >= len(val2):
                result.append((new_path, json.dumps(val1[i]), "<missing>"))
            else:
                find_diffs(val1[i], val2[i], new_path, result)
        return
    
    # Для простых значений
    if val1 != val2:
        result.append((path, json.dumps(val1), json.dumps(val2)))

if __name__ == "__main__":
    main()