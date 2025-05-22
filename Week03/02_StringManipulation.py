# -----------------------------------
# TITLE:    Week 3 - String Manipulation
# AUTHOR:   Clint MacDonald
# DATE:     May 22, 2025
# PURPOSE:  How to work with Strings
# -----------------------------------

# Remembering that strings are actually arrays of characters
my_name = "Clint MacDonald" # array of 15 characters

print(my_name[0]) # C
print(my_name[1]) # l
print(my_name[9]) # D

print(my_name[14]) # d
#print(my_name[15]) # ERROR: index out of range
print(my_name[-1]) # d - always the LAST letter
print(my_name[-3]) # a

print(my_name[:-1]) # Clint MacDonal
print(my_name[:9])  # Clint Mac

print(my_name[3:7]) # nt M
#  given [a:b]  a is inclusive, but b is exclusive
