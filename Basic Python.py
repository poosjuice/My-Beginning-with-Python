from math import sqrt
from math import factorial

# A variable can be made to equal a number, it could be a letter or a word, a phrase or even a simple addition problem

x = 15 * 3
y = 200

# "print" is a crucial function needed for coding
# "print" must always be before whatever code you want to run & whatever you want to print must be in parentheses
# This will print Variable x
print(x)

# This will print Variable y
print(y)

# My examples
a = 10 * 5 - 25
print(a)
b = 131
print(b)

# More complex maths
# This is a video example of a complex method to get a square root

number = 9
print(number**0.5)

# This is the alternative way to get a square root
# In order to use the alternative method you must import the "sqrt" from maths

print(sqrt(number))

# My examples # n = 6
n = 6
print(n**0.5)
m = 16
print(sqrt(m))

# Factorials - the factorial is the distance between 1 & the chosen number
# This example here shows that the factorial is 5
# 5! = 5 x 4 x 3 x 2 x 1

# This first set up shows you the simple way typing out a factorial
print(5*4*3*2*1)

# This set up is useful for larger numbers but in general the quickest way to handle factorials
print(factorial(5))

# My examples
print(6*5*4*3*2*1)
print(factorial(10))
