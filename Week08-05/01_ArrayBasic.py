# --------------------------------------------------
# Title: Week 8 - Introduction to Arrays and Lists 
# Author: Clint MacDonald
# Date: July 3, 2025
# Purpose: Demonstrate array and list basics
# --------------------------------------------------

#region Introduction to Arrays and Lists

''' 
What is an Array!
Is a way to store multiple values within one container.  In Python arrays are actually stored as lists.
------------------------------------
Definitions:
Array:      A way to store multiple values within one container
Element:    Each value in the array
Index:      The position of the element in the array (Starts at 0)'''

my_name = 'Clint'
print(my_name[0])

'''
------------------------------------
An array is a collection of items stored at continuous memory locations.
The idea is to store multiple items of the same type together.
This makes it easier to calculate the position of each element by
simply adding an offset to a base value,
i.e., the memory location of the first element of the array (generally denoted by the name of the array).
------------------------------------
for example: an integer uses 4 bytes of memory and can be represented by  |____| where each _ is a byte of memory.
An array of 5 integers can be represented as follows:
|____|____|____|____|____| - a series of consecutive memory locations of 4 bytes each
If the base address of the array is 2000 and the size of an integer is 4 bytes, then the memory locations of the array
would be as follows:
|2000|2004|2008|2012|2016|  where the name of the array represents the base starting address of the array.
------------------------------------
In Python, the concept of an array technically does not exist, but are in fact lists
which can be used to simulate arrays.  So when we say arrays, we are referring to lists in Python. In other languages, such as C, C++, Java, etc., arrays are a built-in data type and lists are a slightly different type of container.
------------------------------------
Array Basics
- A list is a collection of objects that are ordered and changeable.
- Lists are defined by enclosing the index numbers in square brackets [].
- The elements in a list/array are indexed starting at 0.
- We can access any element in a list using the associated index
- The index of the first element is 0, the second is 1, and so on....
'''
#endregion

#region Array Declaration

myArray1 = []                               # empty list
myArray2 = [ 10, 20, 30, 40, 50 ]           # array of integer
print(myArray2[2])   # 30
myArray3 = [ "apple", "banana", "cherry" ]  # array of strings
myArray4 = [ 10, "apple" , 20.5 ]

#endregion

#region Output of Arrays

print(myArray2)
print(myArray3[2])

print('-'*40)

for i in myArray3:
    print(i)

#endregion

#region Updating and Manipulating Elements in an Array
print('-'*40)
print(myArray3)
print('-'*40)
# changing an element
myArray3[1] = "orange"
print(myArray3)
print('-'*40)

# add a new element
myArray3.append("kiwi")
print(myArray3)
print('-'*40)

# remove elements
myArray3.pop()
print(myArray3)
print('-'*40)

fruit = myArray3.pop(1)
print(fruit)
print(myArray3)
print('-'*40)

# Slicing Arrays/Lists
print('-'*40)
myArray5 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myArray5[2:5])
myArray6 = myArray5[:5]
print(myArray6)
print(myArray5[5:])

#endregion

#region Sorting
print('-'*40)
myArray7 = [ 4, 2, 1, 3, 5]
myArray8 = [ "banana", "apple", "cherry"]

print(myArray7)
print(myArray8)

myArray7.sort()
myArray8.sort()
print(myArray7)
print(myArray8)

#myArray4.sort() - does not work because of mixed data types
#print(myArray4)

#endregion

#region Looping through Array

print('-'*40)
myArray9 = [ 4, 6, 7, 2, 9, 1, 3, 8, 5, 10 ]

for element in myArray9:
    print(element)

print('-'*40)

for index in range(0,10):
    print(myArray9[index])

print('-'*40)
array_length = len(myArray9)
print(array_length)

for i in range(array_length):
    #print(str(i) + " - " + str(myArray9[i]))
    print("%7i - %i" % (i, myArray9[i]))




#endregion