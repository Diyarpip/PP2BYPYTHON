# 1 example

x = 1   # int
y = 2.8 # float
z = 1j  # complex

print(type(x)) # int
print(type(y)) # float
print(type(z)) # complex

# 2 example

x = 1
y = 100
z = 493589734895

print(type(x)) #int
print(type(y)) #int
print(type(z)) #int

# 3 example

a = 1.387295875289
b = 1.0
c = -48.3950

print(type(a)) #float
print(type(b)) #float
print(type(c)) #float

# 4 example

x = 35e3 #e is the same as E and it means the power of 10
y = 34E6
z = -48.2e2

print(type(x)) #float
print(type(y)) #float
print(type(z)) #float

# 5 example

a = 3+5j
print(a.real) #3.0
print(a.imag) #5.0
print(type(a)) #complex

#6 example

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a) #1.0
print(b) #2
print(c) #(1+0j)

print(type(a)) #float
print(type(b)) #int
print(type(c)) #complex

# 7 example

import random #built-in module

print(random.randrange(1, 10)) #print random number from 1 to 10 (10 is not included)