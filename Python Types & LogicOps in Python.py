# Python types
# Here some code will be typed & each line will be showing off a different type

print(type("Hello, world"))  # This is a "str" or String, when using "" with words or phrases
print(type(13))  # This is an Integer, not a decimal or fraction a whole number
print(type(4.72))  # This is a Float, because it has a decimal
print(type(True))  # This is a Bool used for True or False code

# Floats to Integers
# Here we'll take the above Float & show how Floats can be turned into Integers
# Something to note when turning Floats into Integers is that Python will ALWAYS round the number you're converting down

print(4.72, int(4.72))
print(4.05, int(4.05))

# Python is capable of rounding up, but you must code it that way, so now we'll take the same above & round it up to 5

print(4.72, int(4.72), int(round(4.72)))

# My follow up example

print(9.51, int(9.51), int(round(9.51)))

# Turning a String into an Integer
# While it is doable you can only turn Strings with numbers in them into Integers, letters cannot be used

print("12345", int("12345"))

# Turning a types into Float

print(float(18))
print(float("12345"))

# Here we'll move types into a String

print(str(18))
print(str(19.5))
print(type(str(19.5)))

# Logical Operators
# Now we move onto Logic-ops, there are 3 different kinds "and", "or", "not"
# To be noted that Logic-ops can be incorporated into Loops

x = 6
print(x > 0 and x < 10)

y = 23
print(y % 2 == 0 or y % 3 == 0)
# The above code is just determining what "Y" is & determining if it's divisible by 2 or 3
