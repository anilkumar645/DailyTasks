
"""Python program to count occurrence of a given characters in string"""

string = input("Enter from user: ")
char = "P"
count = string.count(char)
print(count)


"""Python program to check if two strings are anagram"""

def anagrams(str1,str2):
    return sorted(str1.lower()) == sorted(str2.lower()) 
print(anagrams("Listen","Silent"))

"""Python program to check a string is palindrome or not"""


s = input("Enter a string: ") #abcdef  

revstr = (s[::-1]) #edcba reverse string 

if revstr == s:
    print("Palindrome")
else:
    print("Not a palindrome")


"""Python program to replace the string space with a given character """

string = input("Enter from user: ")
char = input("Enter char to replace spaces: ")
result = ""

for c in string:
    if c == " ":
        result += char
    else:
        result += c 
print("Modified string: ",result)




"""Python program to replace the string space with a given character using replace() method"""


input_string = input("Enter from user: ")
char = input("Enter char to replace: ")
result = input_string.replace(" ",char)
print("Modified string:",result)


"""Python program to convert lowercase character to uppercase string"""
word = "Python"
result = word.upper()
print(result)

"""Python program to check given character is digit or not using isdigit() method"""

char = input("Enter a character: ")

if len(char) == 1:
    if '0' <= char <='9':
        print(f"'{char}' is a digit.")
    else:
        print(f"'{char}' is not a digit.")
else:
    print("Please enter a single character.")



"""Python program to separate characters in a given string"""

string = input("Enter from user: ")
for char in string:
    print(char)


"""Python program to remove blank spaces from string"""

word = "Hello world"
without_spaces = word.replace(" ","")
print(without_spaces)



"""Python program to concatenate two strings using join() method"""

word1 = input("Enter from user: ")
word2 = input("Enter from user: ")
result = word1 + word2 
print(result)



"""Python program to concatenate two strings without using join() method"""

word1 = input("Enter from user: ")
word2 = input("Enter from user: ")
result = f"{word1}{word2}"
print(result)


"""python program to remove repeated character from string"""

string = input("Enter from user: ")
result = ""
for char in string:
    if char not in result:
        result += char
print(result)



"""Python program to count alphabets,digits and special characters."""

a = input("Enter from user: ")
alphabets = 0
digits = 0
special_chars = 0

for char in a:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits +=1 
    elif not char.isspace():
        special_chars += 1
print(f"alphabets:{alphabets}")
print(f"digits:{digits}")
print(f"special_chars:{special_chars}")


"""Python program to check given character is digit or not"""

char = input("Enter from user: ")
if char.isdigit():
    print(f"'{char}' is a digit")
else:
    print(f"'{char}' is not a digit")


"""Python program to print all non repeating character in a string"""

string = input("Enter from user: ")
for char in string:
    if string.count(char) == 1:
        print(char)


"""python program to copy one string to aother string"""

str1 = "hellow world"
str2 = str1 
print(str2)



"""Python program to print the heighest frequency character in a string"""

str = "Hello World"
max_char = max(set(str),key = str.count)
print(f"Highest frequenct char: {max_char}")
print(f"Frequency: {str.count(max_char)}")




"""python program to calculate sum of integers in string"""


a = "k1y2u3u4"
sum_of_inti = 0
for char in a:
    if char.isdigit():
        a += int(char)
print("Sum of integers: ",sum_of_inti)