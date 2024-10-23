"""positionl aurgements are arguments passed to a function based on their position or order
when calling a function, the first argument corresponding to the first parameter in the functions defination
the second argument to the second parameter,and so on"""


def greet(name,age):
    print(f"Hello , my name is {name} and i am {age} years old")

greet("Alice",25)


def add(x,y):
    print("X -",x)
    print("Y -",y)
    print(x-y)
add(10,20)

def add(y,x):
    print("Y -",y)
    print("X -",x)
    print(x-y)
add(10,20)


"""keyword arguments in python allow to pass values to a function by explicitly specifing the parameter 
names,regardless of their order. this improves the redability of the code and allow more flexibility 
when calling functions"""

def greet(name,age):
    print(f"Hello, my name is {name} and im {age} years old.")
greet(age=30, name="Bob")


"""variable length keyword arguments """


def marks(**l): #kwargs
    for k,v in l.items():
        print(k,"-",v)
    print(sum(l.values()))

marks(m=30,p=50,c=40,e=70,h=60)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name = "Alice",age = 25, location = "New York")


"""default arguments"""

def greet(name , age = 18):
    print(f"Hello , {name}! you are{age} years old.")
greet("Alice")
greet("Bob",25)


def data(email,firstname,lastname = None):
    print(email)
    print(firstname)
    print(lastname)
data("anilkumarvvit@gmai.com","anil","kumar")


