
"""1.Write a Python program to create a list of 5 integers and print the sum of all
 elements in the list.
2.Create a list of strings containing the names of 5 fruits. 
Access and print the second and fourth elements using indexing.
3.Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, 
the last three numbers, and every second number in the list."""

list = [1,2,3,4,5,10,20]
result = sum(list)
print(result)

list = ["Banana","mango","orange","kiwi","graps","apple"]
print("first fruit: ",list[2])
print("fourth fruit: ",list[5])

numbers = [1,2,3,4,5,6,7,8,9,10]
print("first three number:",numbers[:3])
print("last three number:",numbers[-3:])
print("every second number:",numbers[1::2])




"""2.Write a Python program to create a list of 5 integers and print the sum of all
 elements in the list.
2.Create a list of strings containing the names of 5 fruits. 
Access and print the second and fourth elements using indexing.
3.Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, 
the last three numbers, and every second number in the list."""

list = [1,2,3,4,5,10,20]
result = sum(list)
print(result)

list = ["Banana","mango","orange","kiwi","graps","apple"]
print("first fruit: ",list[2])
print("fourth fruit: ",list[5])

numbers = [1,2,3,4,5,6,7,8,9,10]
print("first three number:",numbers[:3])
print("last three number:",numbers[-3:])
print("every second number:",numbers[1::2])





"""3.Write a Python program to create a list of 5 integers and print the sum of all
 elements in the list.
2.Create a list of strings containing the names of 5 fruits. 
Access and print the second and fourth elements using indexing.
3.Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, 
the last three numbers, and every second number in the list."""

list = [1,2,3,4,5,10,20]
result = sum(list)
print(result)

list = ["Banana","mango","orange","kiwi","graps","apple"]
print("first fruit: ",list[2])
print("fourth fruit: ",list[5])

numbers = [1,2,3,4,5,6,7,8,9,10]
print("first three number:",numbers[:3])
print("last three number:",numbers[-3:])
print("every second number:",numbers[1::2])



"""4. Aliasing and Cloning:
1.Create a list of numbers. Assign the list to another variable and modify the original list. 
Check if the second list also changes. Then, create a copy of the original list and show that 
modifying the copy does not affect the original list.
2.Write a Python program to demonstrate how changes in a list's alias affect both lists,
 while changes in a cloned list do not.
"""

l1 = [1,2,3,4,5]
alias_list = l1 
l1.append(6)

print(l1)
print(alias_list)

cloning_list = l1.copy()
cloning_list.append(7)

print(l1)
print(cloning_list)






"""5. Mathematical Operations:
1.Create two lists of numbers, and use the + operator to concatenate them. 
Then, use the * operator to repeat the elements of one list 3 times.
2.Given a list of numbers, write a Python program to create a new list
 where each element is doubled (i.e., each element is multiplied by 2).
"""
list1 = [1,2,3]
list2 = [4,5,6]

modified_list = list1 + list2 
print(modified_list)

repeated_list = list1 * 3 
print(repeated_list)

numbers = [1,2,3,4,5,6]

double_list = [num * 2 for num in numbers]
print("Double list: ",double_list)  





"""6. Membership Operators:
1.Write a Python program to check if a specific element (e.g., 5)
 exists in a given list using the in operator. If it exists, print its position;
   otherwise, print "Element not found."
Given a list of student names, check if "John" and "Sara" are in the list using the in operator."""

students = ["anil","kumar","rahul","john","emma","sarah"]

for name in ["john","sarah"]:
    if name in students:
        print(f"{name} found at position {students.index(name)}.")

    else:
        print(f"{name} not found at position")




"""7. Nested Lists:
1.Write a Python program to create a 3x3 matrix (nested list) and print the matrix. 
Then, access and print the element at row 2, column 3.
2.Create a nested list representing a list of students' 
names and their respective grades. Write a Python program to print each 
student's name along with their grade.
"""

matrix =[[1,2,3],
         [4,5,6],
         [7,8,9]]

element = matrix[1][2]
print("Element at row 2 , column 3: ",element)



students = [["anil",95],
            ["harish",94],
            ["pradeep",93]]

for s in students:
    name , grade = s 
    print(f"{name}:{grade}")
    





"""8. Advanced Challenges:
1.Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:
One containing only the even numbers.
Another containing only the odd numbers.
2.Write a Python program that reads a list of integers and returns 
a new list containing only the unique elements (i.e., removing duplicates).
Given a list of tuples representing (name, age), sort the list by age in ascending order."""


numbers = list(range(1,21))
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even_numbers: ",even_numbers)
print("Odd_numbers: ",odd_numbers)




numbers = [10,20,10,5,3,5,2,20]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:

        unique_numbers.append(num)
print("Unique numbers: ",unique_numbers)
