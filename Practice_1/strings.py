# 1 example

print("Bro")
print('Bro') #same

# 2 example

print("How are you 'Bro?'") #output: How are you 'Bro?'
print('How are you "Bro"')  #output: How are you "Bro"

# 3 example

a = "Bro"
print(a)

# 4 example

a = """GO GO GO 
GO GO GO GO
GO GO GO"""
print(a) # output: GO GO GO 
#GO GO GO GO
#GO GO GO

# 5 example

a = '''GO GO GO 
GO GO GO GO
GO GO GO'''
print(a) # output: GO GO GO 
#GO GO GO GO
#GO GO GO

# 6 example

a = "Bro"
print(a[0]) # B (Start from 0 to n - 1)

# 7 example

for x in "banana":
    print(x) #output will be with enters and letters will be divided by enters
    
# 8 example

a = "Bro"
print(len(a)) #len() give length of string (spaces are counted too)

# 9 example

x = "The best things in life are free!"
print("free" in x) #return True because free is inside of x

# 10 example

x = "The best things in life are free!"
if "free" in x:
  print("Yes, 'free' is present.")
  
# 11 example

x = "The best things in life are free!"
print("expensive" not in x) #vice versa check is not here so return is True

# 12 example

x = "The best things in life are free!"
if "expensive" not in x:
  print("No, 'expensive' is NOT present.")
  
# 13 example

a = "Goodbye!"
print(a[2:5]) # 5 not include (output: odb)

# 14 example

a = "Goodbye!"
print(a[:5]) # 5 not include & automatically start from 0 index (output:Goodb)

# 15 example

a = "Goodbye!"
print(a[2:]) # automatically end until the string is over (output:odbye!)

# 16 example

a = "Goodbye!"
print(a[-5:-2]) # start slicing from the end

# 17 example

a = "Bro"
print(a.upper()) # BRO

# 18 example

a = "Bro"
print(a.lower()) # bro

# 19 example

a = " Br o "
print(a.strip()) #Br o   (only after or before string)

# 20 example

a = "Hello Bro"
print(a.replace("l", "J")) #HeJJo Bro

# 21 example

a = "Hello, Bro"
print(a.split(",")) # returns ['Hello', ' Bro']
# removed ","

# 22 example 

a = "Hello"
b = "Bro"
c = a + b
print(c) #HelloBro

# 23 example

a = "Hello"
b = "Bro"
c = a + " " + b
print(c) #Hello Bro

# 24 example

age = 20
#This will produce an error:
x = "My name is Bro, I am " + age
print(x) # because integer

# 25 example
#f
age = 20
x = f"My name is bro, i am {age}"
print(x) #My name is bro, I am 20

# 26 example

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) #The price is 59.00 dollars

# 27 example

txt = f"The price is {20 * 59} dollars"
print(txt) #The price is 1180 dollars

# 28 example

txt = "We are the so-called "Vikings" from the north." #error

txt = "We are the so-called \"Vikings\" from the north." #correct

# 29 example

txt = "Hello\nWorld!"
print(txt) # /n nwe line

# 30 example

txt = "Hello\tWorld!"
print(txt) # tab

# 31 example

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#32 example 

x = "528"
y = x.isidgit()
print(y) #check is that full digit string and return bool value

# 33 example

x = "BRO"
y = x.isalpha()
print(y) # same thing but with letters

# 34 example

x = "bro"
y = x.islower()
print(y) # same but check is that lower full string

# 35 example 

x = "Welcome Bro!"
y = x.find("Welcome")
print(y) # return index of first letter if this word contained in the string

# 36 example
x = "bro, bro, bro, bro"
y = x.count("bro")

print(y) # return 4