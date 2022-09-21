#  Booleans
# Note when "printing" Booleans you must type "True" & "False" with "T" & "F"


print(True)
print("This is a string")

# Here we show you how to quickly identify what something's "type" is

print(type(True))  # This type is a Bool
print(type("This is a String"))  # This type is a String

# Here we'll show a simplistic explanation of how the True & False works
# All we're doing here is printing wether these statements are true or false
print(5 == 5)  # Just a reminder here the double == sign is essentially to clarify that 5 is 5
print(6 == 5)

# Next will be incorporating an "if Loop" into a boolean

x = 10
y = 5
if x % y == 0:
    print(True)
else:
    print(False)

# Another example will be done here

m = 11
n = 5
if m % n == 0:
    print(True)
else:
    print(False)

# Here we'll explain the "While Loop" with a simple example

number = 1
while number < 4:
    print(number)
    if number == 2:
        break
    number = number + 1  # This code will be taken back through the Loop repeatedly based on what the number we choose is <

# Adding the "else" Statement into the "while Loop"

number = 2
while number < 4:
    print(number)
    number = number + 1
else:
    print("Number is no longer less than 4")

# Here we'll take a look at the "if" Statement within the "while Loop"

number = -10
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")
