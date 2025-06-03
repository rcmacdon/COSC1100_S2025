# -----------------------------
# Week 5 - Data Types
# Clint MacDonald
# June 2, 2025
# Learning how to work with data types
# -----------------------------

# play with data types
myInt = 5
myFloat = 5.0
myString = "Hello"

# print the data type
print(type(myInt))
print(type(myFloat))
print(type(myString))

if (type(myInt) == int):    print("myInt is an integer")
else:                       print("myInt is NOT an integer")


print ((type(myInt) == type(myFloat)))

print (myInt == myFloat)

# isinstance

if (isinstance(myInt, int)): print("is an integer!")

print('-'*60)
myNumber = "5"  # string
print(type(myNumber))
# check if is convertible and if so go ahead and convert it!
if myNumber.isdigit(): myNumber = int(myNumber)
print(type(myNumber))

myName = "clint"
if myName.isdigit(): myName = int(myName)
print(type(myName))