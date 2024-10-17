
#1 question

"write a program that counts the number of even and odd numbers in a list."

n = int(input("Enter input: "))

remainder = (n % 2)

is_even = (remainder == 0)

if is_even:
    print("Even")
else:
    print("odd")


#2 question


"write a program that checks if a given number is prime a prime number is a number greater than 1 that is only divisible 1 and itself"

count = 0 
n = int(input("Enter number: "))

for i in range(1,n+1):
    if n % i == 0:
        count += 1 


if count == 2:
    print("Prime number")
else:
    print("Not a prime number")




# 3 question

s = input("Enter a string: ") #abcdef  
#print(s[:]) #abcdef 
#print(s[0:5]) #abcde 
#print(s[0:5:1]) #abcde 
#maprint(s[::]) #abcde 

revstr = (s[::-1]) #edcba reverse string 

if revstr == s:
    print("Palindrome")
else:
    print("Not a palindrome")




# 4 question


#write a program that prints the number from 1 to 100 
#for multiple of 3 print "Fizz"
#for multiple of 5 print "Buzz"
#for number both multiple five and three print "FizzBuzz"



def Fizz_Buzz(input):

    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    return input
print(Fizz_Buzz(15))





# 5 question 



# number guessing game 

import random

#generate a random number between 1 and 10 
number = random.randint(1,10)

#Promt the user to guess the number 
guess = int(input("Guess a number between 1 and 10: "))

#keep prompting the user to guess until they get it right
while guess != number:
    if guess > number:
        print("Your guess is too high. Try again")
    else:
        print("Your guess is too low. Try again")
    guess = int(input("Guess a number between 1 and 10: "))

print("You guessed it! The number was", number)



# 6 question 

number = int(input("Number: "))
total = 1 

for i in range(1,number+1):
    total += i 
print(total)



# 7 question 


#factorial of a number

number = int(input("Enter a number: "))
factorial = 1 

if number == 0:
    print("Factorial of entered number {} is {}".format(number,factorial))

else:
    for i in range(1,number+1):
        factorial += i 
    print("Factorial of entered number {} is {}".format(number,factorial))
        


# 8 question 

# largest of 3 numbers using if statement 

#first num1 = 56 
#second num2 = 76
#third num3 = 455 

a = int(input("Enter 1st no: "))
b = int(input("Enter 2st no: "))
c = int(input("Enter 3st no: "))

if a>b and a>c:
    max = a;
elif b>a and b>c:
    max = b;
else:
    max = c;
print("Maximum number: ",max)

# 9 question 

# multiplication table for a given number 

n = int(input("Enter number: "))

for i in range(1,11):
    a = n* i 
    print(str(n) +" X " + str(i) + " = " + str(a))

# 10 question 



number = int(input("Enter the number : "))

length = len(str(number))

temp = number 
sum = 0 
while temp >0:
    digit = temp % 10 
    sum += digit ** length 
    temp = temp // 10

print("Number is {} and sum is {}".format(number, sum ))
if sum == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    

