number = int(input())


valid = True  


for digit in str(number):
    
    if int(digit) % 2 != 0:  
        valid = False
        break  


if valid:
    print("Valid")
else:
    print("Not valid")