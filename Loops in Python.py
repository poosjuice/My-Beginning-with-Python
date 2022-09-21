# Key terms appearing here Element / Loop / Statement / Modulus

# Element - Elements are the amount of numbers in between square brackets for lists

# Loop - Loops are a sequence of instruction(s) that is continually repeated until a certain condition is met

# Statement - Statements are lines of code that have been shortened to perform simple tasks without writing out the code for it

# Modulus - Modulus just mean that when they are being used there will be integers with remainders involved

# The focus with Loops here is going to be "for" & "if" Loops, 2 of the most fundamental Python Loops
# Start with creating a list


my_list1 = [5, 10, 15, 20]
# Let's add 5 to each Element in the List
# The "for" Loop will be used in this example

# So this example would be for every Element +5
# Python recognizes "for" as a Loop so when "for" is typed in are you doing a Loop
# This would be written out as seen below & it's vital that a : is used after the List

for element in my_list1:  # Once the : is down a Loop has been started a thin line along the left side will show an indent of your Loop
    element = element + 5  # The input should take our list & +5 to each Element & output [10, 15, 20, 25]
    print(element)

# My example of the "for" Loop
my_list2 = [10, 20, 30, 40, 50]
for element in my_list2:
    element = element / 2
    print(element)

# "if" Loops will be shown here
# "if" Loops are useful in figuring out if large numbers are divisible by a specific number

a = 17
# The % is a Modulus, meaning that it will produce a # with a remainder & that is why there is a 0 before the : because it is a Modular
# Remember after the 0 to put a : to ensure a Loop & indents, indenting ensures the loop is connected
# The double == sign in the Loop is essentially saying that "if a being divisible by 2 = exactly 0 then print"
# The == sign applies to the "if" only

if a % 2 == 0:
    print(
        "a is divisible by 2")  # What the "if" Loop is doing here is taking a variable & printing something based off if it's divisible

else:
    print("a is not divisible by 2")  # In this case 15 is not divisible by 2, so it will print the "else"

# My example of an "if" Loop
b = 24
if b % 2 == 0:
    print("b is divisible by 2")  # This "if" Loop does have a variable that will be divisible by 2 down to 0

else:
    print("b is not divisible by 2")  # It will end up printing the above "if"
