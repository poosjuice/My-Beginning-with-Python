# Operations on Lists
# In this list we have 6 Elements
# When making Lists keep in mind if you have 6 numbers that max amount of Elements you have is 5
# When making the Lists it's always that if you have "n" numbers then you have "n-1" Elements
# The example below will explain that
my_list1 = [1, 2, 3, 4, 5, 6]
# 0th Element = 1
# 1st Element = 2
# 2nd Element = 3
# 3rd Element = 4
# 4th Element = 5
# 5th Element = 6
# Lists always begin from 0 when asking for an Integer
# What we're going to do next is ask for a particular Elements
# In order to do that type out the code, but ensuring that square brackets are used for the chosen Element

print(my_list1[0])
print(my_list1[1])
print(my_list1[2])
print(my_list1[3])
print(my_list1[4])
print(my_list1[5])

# You're also able to do this in reverse
print(my_list1[-1])
print(my_list1[-2])
print(my_list1[-3])
print(my_list1[-4])
print(my_list1[-5])
print(my_list1[-6])

# Let's create slices next, we're going to create a slice from the 2nd Element - 4th Element
# If you refer to the top references at the top lines you'll see our 2nd Element is 3 & the 4th is 5
# Using : in-between the Elements is how you slice what numbers you want to pull from your List
print(my_list1[2:4])

# When slicing keep in mind that it's similar to the Range cmd where you need to account for the second number being -1
# So in this script print(my_list1[2:4]) the printed script would output as [3, 4]
# Tt wouldn't print the 4th Element 5 which is what we want.
print(my_list1[1:5])
# With this above script we have the Elements we're aiming for, with that said it's not the full List either
# This example will ask for the whole list "print(my_list1[0:6])"
print(my_list1[0:6])

# My examples 
my_list2 = list(range(1, 21))
# 0th Element = 1 6th Element = 7
# 1st Element = 2 7th Element = 8
# 2nd Element = 3 8th Element = 9
# 3rd Element = 4 9th Element = 10
# 4th Element = 5 10th Element = 11
# 5th Element = 6
print(my_list2)
print(my_list2[5])  # Remember the Element is the number between the square brackets from the list
# The 5th Element will pull 6 from the list
# A good way to remember this is whatever Elements going between the bracket is being +1
# My slice examples

# Remember that when using Elements you need to account for a -1 or a +1 based on what Elements you are slicing
print(my_list2[0:5]) 
print(my_list2[0:10])
print(my_list2[0:15])
print(my_list2[0:21])
print(my_list2[4:10])
print(my_list2[4:15])

# Simple List Functions
# Length of a list
print(len(my_list1))
print(len(my_list2))

# Maximum & minimum of a list
print(max(my_list2))
print(min(my_list2))

# How to add an Element onto our List
# We'll be using the append function that will put a desired Element on to the end of our list
my_list1.append(7)
print(my_list1)

# This is how to reverse a List for any reason
my_list1.reverse()
print(my_list1)

# Here we'll take 2 Lists & put them together
# Very simply just type out "print(my_list3 + my_list4)"
my_list3 = [10, 20, 30, 40, 50]
my_list4 = [60, 70, 80, 90, 100]
print(my_list3 + my_list4)
# You can also set it up like this
print(my_list4 + my_list3)  # Whatever goes before the + is the List that will be outputted first
