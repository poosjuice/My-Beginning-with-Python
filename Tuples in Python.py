# In this file we'll be looking at Tuples

# Tuples - Tuples are similar to lists that they are a sequence of items made up of any type
# Worth noting that they cannot have their Elements modified like normal Lists

# Here we'll set up an example Tuple, so we know what it looks like

# Conventionally, Tuples look like this
# Another telltale of Tuples is that they use ()brackets while Lists use [] brackets
Fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6)  # This is the Tuple, uses ()

List_of_Fruit = ["Apples", 4, "Bananas", 5, "Oranges", 6]  # This is a List, uses []

print(List_of_Fruit)
print(type(Fruit))
print(type(List_of_Fruit))

# Lists CAN be modified
# Just as a refresher we'll show you can modify Elements within a List

List_of_Fruit[0] = "Strawberries"  # We're trading out the 0th Element or "Apples" for "Strawberries"
print(List_of_Fruit)

# Now we'll show an example that Tuples CANNOT be modified
# Fruit[0] = "Strawberries"
# print(Fruit) # When this code is run we get an error telling us there's no support for "item assignment"

# Even with differences some similar operations can be done on Tuples like Lists

print(Fruit[0:3])   # Here we can slice for specific Elements from the Tuple just as if it was a List
# So with this we are asking it to print the Tuple from the 0th-3rd Element just the same as we can a List
# Worth noting that the Strings within the Tuple as well as the Integers as their own argument each

# Here we'll do the same thing & request the whole Tuple for example

print(Fruit[0:5])

# We can also just recall specific Elements within a Tuple too

print(Fruit[0])  # This will recall "Apples"
print(Fruit[5])  # This will recall "6"

# Concatenations can be done with Tuples also, so here we'll see examples

Fruit = Fruit[0:4] + ("Cherries", 10)
print(Fruit)

# Tuples with 1 Element

# In order for a Tuple to have 1 Element it needs to have a , in it
x = (5, )  # This is a Tuple
print(type(x))
y = 6  # This is an Integer
print(type(y))

# Tuples can have their Lists determined through code as well.
print(len(Fruit))

# Creating a Tuple
my_tuple = tuple(("Hello", 18, True))
print(type(my_tuple))

# Next we'll show how to convert a Tuple into a List & back
# We're converting it to a List in order to add Elements to the end
# Then we convert it back to a Tuple

Fruit = list(Fruit)  # This code turns the Tuple into a List
Fruit.append("Pears")  # Now that it's a List we can append "Pears" to it
Fruit = tuple(Fruit)  # After the line for the "Pears" is added this code turns it back into a Tuple
print(Fruit)

# Here we're unpacking Tuples & what that entails

Fruit = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
# So we create a Tuple using the above Strings

(one, two, three, four, five) = Fruit  # This Tuple is assigning these Variables
# After creating the Tuple with this code we're basically assigning each String a variable

print(five)
print(four)

# Incorporating Loops with Tuples
for x in range(len(Fruit)):
    print(Fruit[x])
