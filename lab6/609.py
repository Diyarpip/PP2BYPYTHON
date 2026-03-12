
n = int(input())


keys = input().split()  
values = input().split()  

dictionary = dict(zip(keys, values))

query = input()

if query in dictionary:
    print(dictionary[query])
else:
    print("Not found")