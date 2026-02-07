n = int(input())  

unique_surnames = set()


for _ in range(n):
    surname = input().strip()  
    unique_surnames.add(surname)  


print(len(unique_surnames))