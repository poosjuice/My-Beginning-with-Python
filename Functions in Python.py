# Key terms appearing in here:

# String - A String is a series of any characters that are within quotation marks that are interpreted literally by a script

# Functions - Functions are a block of code created to simplify coding, most Functions are already created but anyone can create their own with know-how

# In this file we'll take a closer look at Functions
# Functions in Python are similar to normal maths, where a function takes an argument & produces a result
# Below we'll show how a Function would be set up

# The general form of a Python Function is:
# def function_name(argument):
# (lines of code telling what the function to do)
# return result

# Below this comment we'll show an actual bit of code using a Function
# So let's consider producing a function that returns x^2 + y^2
# Our Function can be written as anything we choose as long as it's one word

def squared(x, y):  # So the Function here is "squared" & the Arguments are "x, y"
    result = x ** 2 + y ** 2
    return result


print(squared(5, 5))


# Another Function example

def born(country):
    return print("I am from " + country)


born("America")


# My example

def born(city):
    return print("I was born in " + city)


born("Oceanside, California")


# Another example from me
def born(state):
    return print("I used to live in Ohio, then I had to move to " + state)


born("Arizona")
