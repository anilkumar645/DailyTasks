


""" 1.Define a function called `greet` that takes a name as an argument 
 and prints a greeting message like:"Hello, [name]!"""

def greet():
    name = input("Enter from user: ")
    print(f"Hello, {name}!")
greet()


""" 2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. 
 Test the function by passing different numbers."""

def add():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Sum: " , a+b)
add()


"""3.Create a function `is_even` that takes a number as an argument and returns `True` 
if the number is even, and `False` otherwise."""


def is_even():
   number = int(input("Enter a number: "))
   print("is_even:", number % 2 == 0)
is_even()


"""4.Write a function `factorial` that takes a positive integer as input and returns the factorial of that number.
 Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\)."""


def factorial():
    n = int(input("Enter a positive integer: "))
    result = 1 
    for i in range(1,n+1):
        result *= i 
    print("Factorial:",result) 
factorial()

"""5.Define a function `find_max` that takes three numbers as input and returns the largest of the three.
 Test the function with various sets of numbers."""

def find_max():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the first number: "))
    c = float(input("Enter the first number: "))
    print("Max:",max(a,b,c))
find_max()

"""6.Write a function `count_vowels` that takes a string as input and returns
 the number of vowels (a, e, i, o, u) in the string."""

def count_vowels():
    string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char in vowels)
    print("Vowels Count: ",count)
count_vowels()



"""7.Create a function `is_prime` that takes a number as input and returns
 `True` if the number is prime, and `False` otherwise."""

def is_prime():
    n = int(input("Enter a number: "))
    if n <= 1:
        print("Not Prime")
        return 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            return 
        print("Prime")
is_prime()



"""8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the 
sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\)."""


def recursive():
    n = int(input("Enter a positive integer: "))
    print("Recursive Sum:",recursive(n))


"""9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). 
The function should perform the operation on the two numbers and return the result."""


def calculator ():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operator = input("Enter an operator(+,-,*,/): ")
    if operator == "+":
        print("Result:", a+b)
    elif operator == "-":
        print("Result:", a-b)
    elif operator == "*":
        print("Result:", a*b)
    elif operator == "/":
        print("Result:", a/b)
    else:
        print("Division by zero is not allowed.")
calculator()



"""10.Write a function `find_common_elements` that takes two lists as input and returns
 a list of elements that are present in both lists."""

def common_elements():
    list1 = input("Enter the first line of element separated by spaces: ").split()
    list2 = input("Enter the second line of element separated by spaces: ").split()
    common_elements = list(set(list1) & set(list2))
    print("Common Elements: ",common_elements)

common_elements()




"""11.Write a function `reverse_string` that takes a string as input and returns the string reversed."""


def reverse_string():
    string = input("Enter a string: ")
    print("Reversed String: ",string[::-1])
reverse_string()


"""12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples sorted
 by the dictionary values in ascending order.
"""
def sort_dict_by_value():
    d = {}
    n = int(input("Enter items in dictionary: "))
    for i in range(n):
        key = input("Enter key:")
        value = input("enter value:")
        d[key] = value 
    sorted_dict = sorted(d.items(),key = lambda item: item[1])
    print("Sorted Dictionary by Value:",sorted_dict)
sort_dict_by_value()

