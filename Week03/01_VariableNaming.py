# -----------------------------------
# TITLE:    Week 3 - Variable Naming and Style Guide
# AUTHOR:   Clint MacDonald
# DATE:     May 22, 2025
# PURPOSE:  To demonstrate the basics fo variable naming and style guide
# -----------------------------------

import math

# Variable names are used to store data in a program. 
#     They are used to reference data in memory.

# appropriate for the student's first name
first_name = "Clint"        # decent - could be more specific
student_fname = "Clint"     # Unacceptable - abbreviation
student_name = "Clint"      # bad - could be full name
studentFirstName = "Clint"  # Good - camel case
StudentFirstName = "Clint"  # Unacceptable - pascal case
student_first_name = "Clint"# Good - snake case
studentfirstname = "Clint"  # Bad - not camel case
fName = "Clint"             # Unacceptable
Std_First_Name = "Clint"    # Unacceptable (S)

# Camel case - is each word capitalized except the first one
# Pascal Case - all words capitalized
# Snake Case - Words divided by underscore

# camel case of snake case is often used to represent storage locations
# pascal case is used for objects

FIRSTNAME = "Clint"         # Unacceptable
BACKGROUND_COLOR = "Black"  # Good - assuming it will not change
PI = 3.14                   # Good
VIN = "DB45EF23A673B"       # Unacceptable - abbreviation, all caps

# 2 or 3 shortcuts I will accept
# id  instead of identification
# num  instead of number
vehicle_id_num = "DB45EF23A673B"
vehicleIdNum = "DB45EF23A673B"

speed_of_light = 299792458  # Bad - it should be a constant
SPEED_OF_LIGHT = 299792458  # Good
c = 299792458 

celsius = -14
fahrenheit = (9 / 5) * celsius + 32

TEMPERATURE_CONVERSION_RATIO = 9.0 / 5.0
TEMPERATURE_CONVERSION_CONSTANT = 32

fahrenheit = TEMPERATURE_CONVERSION_RATIO * celsius + TEMPERATURE_CONVERSION_CONSTANT


# x squared
x = 5
x_squared = x ^ 2
x_squared = x ** 2
x_squared = x * x

# pythagorean theorem
# given a triangle
a = 5
b = 12

c = (a **2 + b ** 2) ** 0.5

c = math.sqrt( math.pow(a,2) + math.pow(b,2))

