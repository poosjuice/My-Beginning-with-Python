# Working on Lists the list shown has 6 Elements
#  are the amount of characters/numbers within the square brackets
# This list example is meant to show "6 people & how many pairs of shoes each person owns"
# When Lists are typed out normally as seen below they will output exactly as shown when ran

my_list1 = [1, 2, 3, 4, 5, 6]

# To create a list without typing out the entire number set you can use the Range cmd
# Using the Range cmd will create a list numbers given & in this example 1-6
# When using the Range cmd to create a list it will always take the final list number & subtract it by 1
# That means that this list below when printed will show up as [1, 2, 3, 4, 5]

my_list2 = list(range(1, 6))
print(my_list1)
print(my_list2)

# My examples

my_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list4 = list(range(1, 10))
print(my_list3)
print(my_list4)

# Arguments are the amount of numbers in parentheses right after the Range cmd
# In the Lists below List5 has 2 Arguments & List6 has 3 Arguments
# There can only be 3 Arguments max or there will be an error

my_list5 = list(range(1, 61))
print(my_list5)
my_list6 = list(range(1, 105, 10))
print(my_list6)

# What the 3rd Argument does is takes the list of numbers inputted & goes up the list by that number +1
# In this example we'll see the 3rd Argument take the first two numbers to create the List thereon

my_list7 = list(range(1, 22, 2))

# So in this example the list created from the code above is [1, 3, 5, 7, 9, 11] & so on
# This example take 1 & 22 to create a list but takes the 3rd Argument & creates the list going upwards of 2 each time
# 1 + 2 = 3, 3 + 2 = 5, 5 + 2 = 7, 7 + 2 = 9 & so on thus making our List [1, 3, 5, 7, 9, 11]

print(my_list7)
