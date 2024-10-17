

"""Extended slicing"""

# variabel[start_index : end_index]

"""Along with start_index , and end_index we will provide step
 The step determine between each index for slicing"""

"""for example"""

message = "-A-N-I-L-"
print(message[1:8:2])

"output is ANIL"

print("--------------------------------------------------------")

a = "waterfall"
part = a[1:6:3]
print(part)

"output is ar"


"""python has build-in resuable utilities.They simplify the most commonly performed operations are

STRING METHODS 


1.isdigit()
2.strip()
3.lower()
4.upper()
5.startswith()
6.endswith()
7.replace()

"""

"gives true if all characters are digit"

is_digit = "5454".isdigit()
print(is_digit)

"output True"

"remove ll leading and trailing spaces from string"

mobile = "9121626318"
mobile = mobile.strip()
print(mobile)

"output 9121626318"


"we can also specify characters that need to be removed"

name = "ANIL."
name = name.strip(".")
print(name)

"output Ravi"


"Remove all spaces ,comma(,) and fulstop(.) that lead or trail string"

name = ", .. ,, ravi ,, "
name = name.strip(" ,.")
print(name)

"output ravi"


"""gives a new string after replacing all the occurance of the 
old substracting with new substring"""

sentence = "teh cat and teh dog"
sentence = sentence.replace("teh" ,"the")
print(sentence)

"output the cat and the dog"


"give a new string be converting each character of the given string to uppercase"

name = "ravi"
print(name.upper())

"output RAVI"


"""Gives a new string by converting each 
character of the given string to lowercase"""

name = "RAVI"
print(name.lower())

"output ravi" 


"""Membership check in python is used to verify if a value exists in a SEQUENCE (such as a list,string
tuple or set)"""

"Membership operators"

"""1.in: check if the value present in a sequence

    2. not in : check if a value is not present in a sequence"""

#LIST
my_list = [1,2,3,4,5]
print(3 in my_list) #output True 
print(6 in my_list) #output False  


#TUPLE 
my_tuple = (1,2,3,4,5)
print(3 in my_tuple) #True 
print(6 in my_tuple) # False 

#STRING 
my_string = "hello"
print('h' in my_string) #output: True 
print('x' in my_string) #output: False 

#SET 

my_set = {1,2,3,4,5}
print(3 in my_set) #output True 
print(6 in my_list) #output False 

"""USAGE
1.data validation
2.data filtering 
3.checking for duplicates 
4.verify user input
"""