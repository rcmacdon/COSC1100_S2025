# ----------------------------------
# Title: COSC1100 - Learning Basic DataTypes
# Author: Clint MacDonald
# Date: May 15, 2025
# Purpose: Learning Data Types and Math
# ----------------------------------

# MAIN DATA TYPES - Native

# Character - 1 character - 1 Byte Memory (8 bits)
#                        - 8 digit binary number - 256 different combinations
# Integer   - whole number - 4 Bytes (32 bits)  (2^31) 
#           - largest number approx 2.14 Billion
# Float     - fractions - less memory than decimal
# Decimal   - larger fractions
# Boolean   - true or false, 1 or 0, yes or no

# non-native types
# String    - multiple characters - array of characters
# Date also includes Time   - stored as floating point decimals
#                           - units are days since jan 1, 1900

# - Memory
'''
1 bit = 1 binary digit (0 or 1)
1 byte = 8 bits (256 possible values)
1 kB - kiloByte = 1024 bytes
1 MB - MegaByte = 1024 kB 
1 alphanumeric character takes 1 byte of memory (ASCII - character set)
'''

# Variable Declarations
# integers
xi = 2
yi = 6
# Floats
xf = 2.1
yf = 6.0
# Strings
xs = "2"
ys = "6"
# Boolean
xb = True
yb = False

# mathematics
print(xi+yi)
print(xf+yf)
print(xs+ys)
print(xb+yb)

# mixing them
# print(xi + ys)  - ERROR
# print(xs + yi)  - ERROR
print(xi + yf)  # 8.0
print(xf + yi)  # 8.1

# division
print(7/3) # 2.333333333..
print(7//3) # integer math = 2

print("The answer is: %.2f" % (7//3)) 