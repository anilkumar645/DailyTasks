 
"""Write a python program to merge two list?"""

list_a = [1,2,3,4]
list_b = [0,*list_a,5,6,7,8]
print(list_b)


"""Write a python program to delete element of given index in list ?"""

list_a = [0,1,2,3,4,5]
result = list_a.index(int(input(("Enter from user: "))))
list_a.remove(result)
print(list_a)


"""Write a python program to delete given element from the list?"""

list_a = [0,1,2,3,4,5,6]
list_a.remove(int(input("Enter from user: ")))
print(list_a)


"""Write a python programe to check if the two list are having atleast one common element?"""

a = [0,1,2,3,4,5]
b = [0,9,10,4,6,8,7]

common = [item for item in a if item in b] 
print(common)

"""Write a python program to remove  specified column from the nestedlist?"""

nested_list = [[1,2,3],
                [4,5,6],
                [7,8,9],]
col_index = 1 
for row in nested_list:
    del row[col_index]
print(nested_list)


"""Write python program to convert a list of integers into single integer ?"""

numbers = [1,2,3,4,5,6]
single_integer = 0 
for num in numbers:
    single_integer = single_integer * 10 + num 
print(single_integer)

"""Write  a python programe to remove duplicates from the list ?"""

numbers = [1,2,3,4,5,6,6,7,7]
unique = list(set(numbers))
print(unique)


"""Write a program to create a set."""

set = {1,2,3,4,5}
print(set)


"""Write program to iterate over sets."""
set = {1,2,3,4,5}

for item in set:
    print(item)

"""Write a Python program to add number to a set."""
set_a = {1,2,3}
set_a.add(4)
set_a.update([5,6,7,8])
print(set_a)

"""Write a Python program to remove item from a given set."""

my_set = {1,2,3,4}
my_set.remove(3)
print(my_set)



"""Write a python program to create a intersection of set ?"""

set_a = {1,2,3,4,5,6}
set_b = {4,5,6,7,8,9}

result = set_a.intersection(set_b)
print(result)

"""Write a python program to createa union of set ?"""
a = {1,2,3,4,5}
b = {5,6,7,8,9}
union = a.union(b)
print(union)


"""Write a python program to create set differance ?"""
l = {1,2,3,4,5}
m = {6,7,8,9}
difference = l.difference(m)
print(difference)

"""Write a python program to create a symmetric defferance ?"""

a = {1,2,3,4}
b = {3,4,5,6}

symmetric_difference_set = a.symmetric_difference(b)
print(symmetric_difference_set)



"""write a python program to find max and min values in a set?"""

my_set = {10,20,30,40,50,60}
max_value = max(my_set)
print(max_value)

min_value = min(my_set)
print(min_value)


"""Given two Python sets, write a Python program to update the first set with items that exist only 
in the first set and not in the second set.""""

set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}
set_1.difference_update(set_2)
print(set_1)


"""Write a Python program to remove items 10, 20, 30 from the following set at once.?"""

sample_set = {10,20,30,40,50}
sample_set .difference_update({10,20,30})
print(sample_set)

"""Check if two sets have any elements in common. If yes, display the common elements?"""

set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}

common_elements = set_1.intersection(set_2)
if common_elements:
    print("Common elements: ",common_elements)
else:
    print("No common elements.")


"""Update set1 by adding items from set2, except common items?"""
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}

set_1.symmetric_difference_update(set_2)
print(set_1)

"""Remove items from set1 that are not common to both set1 and set2?"""
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}

set_1.difference_update(set_2)
print(set_1)


"""How do you create a empty tuple on python ?"""

empty_tuple = ()
print(empty_tuple)

"""Write a python program to unpack atuple into several variables ?"""

tuple_data = (1,2,3)
a,b,c = tuple_data 
print(a,b,c)



"""write a python program to add an item to the tuple ?"""

tuple_data = (1,2,3)
tuple_data = tuple_data + (4,)
print(tuple_data)

"""Write a python proram to convert tuple into a string ?"""

data = ('h','e','l','l','o')
tuple_string = ''.join(tuple_data)
print(tuple_data)

"""Write a python program to find most frequent element in tuple ?""""

tuple_data = (1,3,2,1,4,1,2,3)
most_frequent = max(tuple_data, key = tuple_data.count)
print("Most frequent element: ",most_frequent)



"""1	Write a python program to  add a key to a dictionary ?"""

sample_dict = {1:10,2:20}
sample_dict[3] = 30
print(sample_dict)

"""2	Write a python program to check weather the given value is present in the dictionary or not ?"""

sample_dict = {1:10,2:20,3:30}
value_to_check = 20
if value_to_check in 
sample_dict.values()
print(f"{value_to_check} is not present in the dictionary")
else:
print(f"{value_to_check} is not present in the dictionary.")


"""3	Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}"""

square_dict = {x: x** 2 for x in range(1,16)}
print(1,16)

""" 4 Write a python program to create a dictionary from the string ?"""

string = "python"
char_count = {char: string.count(char) for char in string}
print(char_count)


"""Write a python program to combine two dictionaries by adding values of common keys ?"""

dict1 = {'a':10,'b':'20','c':30}
dict2 = {'b':5,'c':'15','d':40}
for key in dict2:
    if key in dict1:
        dict1[key] += dict2[key]
    else:
        dict1[key] = dict2[key]
print(dict1)
         

"""6	Write a python program to merge two python dictionaries ?"""

dict1 = {'a':10, 'b':20}
dict2 = {'b':30, 'c':40}
dict1.update(dict2)
print(dict1)

"""7	Write a Python program to create a dictionary from a string.  Note: Track the count of the
 letters from the string."""

"""Sample string : 'skywavessoftwares'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
 """

string = 'skywavessoftwares'
letter_count = {}

for letter in string:
    if letter in letter_count:
        letter_count[letter] += 1 
    else:
        letter_count[letter] = 1 
print(letter_count)

