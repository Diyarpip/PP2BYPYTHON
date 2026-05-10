# 1 example

x = "Hello man!"
print(type(x)) #string

x = 21
print(type(x)) #int

x = 20.5
print(type(x)) #float

x = 3j
print(type(x)) #complex <class 'class'> 'class' = complex
z = 3 + 4j
print(z.real) # 3.0
print(z.imag) # 4.0

x = ["What", "just", "happened"]
print(type(x)) #list

x = ("milk", "banana", "meat")
print(type(x)) #tuple

x = range(3, 10) #[3, 4, 5, 6, 7, 8, 9] 
print(type(x)) #range 

x = {"name" : "Bro", "age" : 12}
print(type(x)) #dict

x = {"cucumber", "Rage", "btw"}
print(type(x)) #set

x = frozenset({"Smile", "my", "friend"})
print(type(x)) #frozenset

x = True
print(type(x)) #bool

x = b"GET OUT"
print(type(x)) #bytes

x = bytearray(3)
print(type(x)) #bytearray

x = memoryview(bytes(7)) 
print(type(x)) #memoryview

x = None
print(type(x)) #Nonetype

# 2 example
#specifying

x = str("Go")
print(type(x))

x = int(123)	
print(type(x))

x = float(89.5)		
print(type(x))

x = complex(1j)		
print(type(x))

x = list(("What", "are", "you?"))	
print(type(x))	

x = tuple(("Are", "you", "sure?"))	
print(type(x))

x = range(15)	
print(type(x))

x = dict(name="Bro", age=12)	
print(type(x))	

x = set(("Who", "Elder", "King"))	
print(type(x))	

x = frozenset(("no", "more", "sugar"))	
print(type(x))	

x = bool(8)	
print(type(x))

x = bytes(65)		
print(type(x))

x = bytearray(23)	
print(type(x))	

x = memoryview(bytes(30))
print(type(x))