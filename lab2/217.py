n = int(input())


numbers = []
for _ in range(n):
    numbers.append(input().strip())


already_checked = []
result = 0


for number in numbers:
    
    if number not in already_checked:
        
        count = 0
        for other in numbers:
            if number == other:
                count += 1
        
        
        if count == 3:
            result += 1
        
        
        already_checked.append(number)

print(result)