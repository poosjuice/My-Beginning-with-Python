# Today is looking at Strings in more depth

# We've already covered Strings, Integers, Floats,  Booleans, & Lists
# Integers, Floats, & Booleans are all considered simple data types
# That means that they cannot be broken down

# Lists & Strings are different, they are made from smaller pieces
# This just means that they CAN be broken down

# We already know what Strings are, words or phrases within "" that are in lines of code
print("Hello, world")
print(type("Hello, world"))

# Next is some operations on Strings
# The first thing we'll show is Addition sign concatenation

Greeting = "Hello"
Name = "Robbie"
print(Greeting + Name)

# Next we look at the * Operator
# The * Operator allows String we create to be multiplied

print(Name*3)
print(Greeting + Name*3)
print((Greeting + Name)*3)

# Next we'll look at the Index Operator
# Index Operator allows us to pull the specified Element from our String

print(Name[2])
print(Name[1] + Name[4])
# Here we have code to pull the 1st & 4th element from "Name" which should be "o", "i"

# Next we're onto slicing operations

print(Name[0:3])
print(Name[3:6])
print(Name[:6])

# Next up is Uppercase & Lowercase which will make Strings you code be all uppercase or lowercase
# We'll be using "Name" still which is = "Robbie" currently

print(Name.lower())  # The lower codes the String into all lowercase
print(Name.upper())  # The upper codes the String into all uppercase

# Next up is counting how many times characters appear in Strings

print(Name.count("b"))

# Characters within Strings can also be replaced specifically too

print(Name.replace("R", "B"))

# Formatting Strings

# your_name = input("Your name: ")
# hello = "Hello {}".format(your_name)
# print(hello)

# Each letter in Python is assigned a specific number

print("orange" < "strawberry")
print("blue" > "orange")

# Here we'll take a look at the "in" & "not" Operators

fruit = "bananas"
print("a" in fruit)
print("s" in fruit)

# Now we'll mix together a few things learned recently

x = "hello"
y = ""
for character in x:
    y = character.upper() + y
print(y)
