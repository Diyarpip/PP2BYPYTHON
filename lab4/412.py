import json

obj1 = json.loads(input())
obj2 = json.loads(input())

differences = []

def compare(o1, o2, path=""):
    # Если оба значения — словари, сравниваем по ключам
    if isinstance(o1, dict) and isinstance(o2, dict):
        keys = set(o1.keys()) | set(o2.keys())
        for key in keys:
            new_path = f"{path}.{key}" if path else key
            if key in o1 and key in o2:
                compare(o1[key], o2[key], new_path)
            elif key in o1:
                differences.append(
                    f"{new_path} : {json.dumps(o1[key], separators=(',', ':'))} -> <missing>"
                )
            else:
                differences.append(
                    f"{new_path} : <missing> -> {json.dumps(o2[key], separators=(',', ':'))}"
                )
    else:
        # Если значения разные — фиксируем различие
        if o1 != o2:
            differences.append(
                f"{path} : {json.dumps(o1, separators=(',', ':'))} -> {json.dumps(o2, separators=(',', ':'))}"
            )

compare(obj1, obj2)

if differences:
    for line in sorted(differences):
        print(line)
else:
    print("No differences")