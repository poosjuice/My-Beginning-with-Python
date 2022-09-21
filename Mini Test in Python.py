import matplotlib.pyplot as plt

# In this file a mini test of what I've learned will be done
# I'll be taking questions from the individual in the video im learning from
# Then apply what I've learned to solve given task

# The first task of the mini test will be creating two variables with Integers I've given said Variables
# The code to be pulled off here will take whatever we assign to the Variables
# Then Performing some basic math on them

# First we assign Variables "x" & "i"
x = 131
i = 5

# With these Variables now assigned we'll do 4 basic maths with them

print(x + i)  # This is addition our Variables
print(x % i)  # This is dividing our Variables
print(x - i)  # This is subtracting our Variables
print(x * i)  # This is multiplying our Variables

# The 2nd task will be making a List doing specific task within that List

mylist = list(range(0, 102, 2))  # Here a List was created from 0-100 going up by 2's only
print(len(mylist))
print(mylist)
print(mylist[0:11])  # This will print the first 10 Elements from our List above

# The last part of this 2nd task will have us Append whatever type to the end of this List
print(mylist.append("example"))
print(mylist)

# In this 3rd task I'll be taking a Variable & giving it an Integer then
# Using "if" Loops determine wether this Variable is divisible by 5
# Then have Python print wether it is or isn't

r = 131  # Assigning "r" to 131
if r % 5 == 0:  # The code basically asking if "r" is capable of being divided by 5
    print("r is divisible by 5")
else:
    print("r is not divisible by 5")

# For the 4th task a "for" Loop will be used to print the numbers 0 - 5
for i in range(0, 6):
    print(i)

# Another quick example to just go a bit further 0 - 10
for r in range(0, 11):
    print(r)


# The 5th task wants a pentagon drawn with Turtle, VSCode may be using Python
# but some packages/imports are not a part of VSCode in this case Turtle, thus limiting some of what can be done
# Regardless the code for it will be typed out here for reference

# Starting out "Turtle" would be imported so:
# import turtle

# A "for" Loop will be used here to shorten code

# for r in range(5):   - The 5 is there because a pentagon has 5 sides
#     turtle.right(72)    - The 72 is the angle need to make a pentagon
#     turtle.straight(100) - The 100 will be the distance between each formed line
# turtle.done()


# The 6th task is creating a Function & test wether a,b, & c are a Pythagorean Triple

def pythagorean_triple(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


print(pythagorean_triple(3, 4, 5))  # This is a PythaTriple
print(pythagorean_triple(8, 3, 5))  # This is not

# Task #7 wants an error in some written code to be spotted/pointed out
# Below is the code in hashtag

# n = 5
# while n > 0  - Right here after the "0" there should be a :
# n = n + 1    - The colon helps keep it altogether in it's "Loop"
# print(n)

# Task #8 wants 2 Lists created of size 5 or choice
# Then plot these Lists against each other

# First off an import is needed, said import is, look at the top as imports are always first

list1 = [1, 6, 13, 16, 24]
list2 = [3, 7, 17, 28, 30]
plt.plot(list1, list2, c="blue", linewidth=1, label="A Line",
         linestlye="dashed", marker="s", markerfacecolor="purple", markersize=2)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Python plot of a line")
plt.legend()
plt.show()
