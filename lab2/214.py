n = int(input())  
numbers = list(map(int, input().split()))  

max_count = 0
result = numbers[0]


for num in numbers:
    
    current_count = 0
    for other in numbers:
        if num == other:
            current_count += 1
    
    
    if current_count > max_count:
        max_count = current_count
        result = num
    
    elif current_count == max_count and num < result:
        result = num

print(result)