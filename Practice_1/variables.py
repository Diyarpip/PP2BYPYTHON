# 1 example
x = 100 # x type is int
y = "Who" # y type is string
print(type(x)) # output int
print(type(y)) # output string

x = str(100) # x will be '100'
x = int(100) # x will be 100
x = float(100) # x will be 100.0

x = "Bro"
# is the same as
x = 'Bro'

a = 400
A = 'Bro'
#A will not overwrite a

# 2 example
2you = "John"
my-var = "John" #illegal names of variables
lol h = "John"

# 3 example
x, y, z = "Bro", "Banana", "Cucumber" #allow to declare three of them
print(x); print(y); print(z)

x = y = z = "Bro" #allow to declare three of them
print(x); print(y); print(z)

bro = ["who", "me", "eee"] #collection
x = y = z = bro
print(x); print(y); print(z) #output: who
#me
#eee

# 4 example
x, y, z = "B", "C", "D"
print(x, y, z) #output: "B C D"

x, y, z = "B", "C", "D"
print(x + y + z) #output: "BCD"

x = 5; y = 10
print(x + y) # output 15

x = 5
y = "Bro"
print(x + y) #error

x = 5
y = 'Bro'
print(x, y) #5 Bro

# 5 example
x = "Bro!" #global variable can be used everywhere

def func():
    print("Hello " + x)

func()
######
x = "Bro!" #global

def func():
    x = "WHO?" #only inside in function (local)
    print("Hello " + x)

func()

print("Hello " + x) 
######
x = "awesome"

def myfunc():
  global x #change global variable of x
  x = "useless"

myfunc()

print("Python is " + x)


