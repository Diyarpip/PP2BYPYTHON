n = int(input())

db = {}   

for i in range(n):
    line = input()         
    parts = line.split()   

    if parts[0] == "set":
        key = parts[1]
        value = parts[2]
        db[key] = value   

    if parts[0] == "get":
        key = parts[1]
        if key in db:
            print(db[key])
        else:
            print("KE: no key", key, "found in the document")
