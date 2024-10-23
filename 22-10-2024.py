l = [1,2,3,4,5,6,7,8,9]

total = len(l)
for i in l:
    total = total + 1
print(total)
print(len(l)) 


def get_even(l):
    if l % 2 == 0:
        return True
    else:
        return False
    
l = [1,2,3,4,5,6,7,8,9]
f = filter(get_even,l)
print(list(f))


l = lambda x,y : x if x>y else y
print(l(500,20))




"""reduce()"""
from functools import * 
l = [1,2,3,4,5,6,7,8,9]
rs = reduce(lambda x,y : x+y,l)
print(rs)


"recurrsion"

def factorial(z):
    if z == 0:
        return 1 
    else:
        return (z * factorial(z-1))
print(factorial(5))
