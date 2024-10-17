
#reverse the string

s = "learning python is very easy"
revstr = (s[::-1])

print(revstr)


#Removing spaces 

word = "learning python is very easy" 

result = "".join(word.split())
print(result)


# reverse word by word 

string = "learning python is very easy"  

word = string.split()
rev_string = ""

for word in reversed(word):
    rev_string += word + " "

print(rev_string.strip())


# how many characters in a string 


s = "learning"
for char in s:
    print(f"{char} = {s.count(char)}")