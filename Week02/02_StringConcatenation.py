# ----------------------------------
# Title: COSC1100 - Learning Strings and Formatting
# Author: Clint MacDonald
# Date: May 15, 2025
# Purpose: Learning Strings and Formatting
# ----------------------------------

# String Concatenations
first_name = "Clint"
last_name = "MacDonald"
student_id = 123456789

# concatenate these
full_name = first_name + " " + last_name + " (" + str(student_id) + ")"

# Formatting

print('--------------------------')
print("Hello, my name is " + full_name + ".")
print("Hello, my name is", full_name, ".")
print(f"Hello, my name is {full_name}.")
print("Hello, my name is {}.".format(full_name))
print("Hello, my name is %s." % full_name)
print('--------------------------')
print("Hello, my name is %s %s (%i)." % (first_name, last_name, student_id))
print('--------------------------')
print("Hello, my name is %s %s (%i).\n\tHello World!" % (first_name, last_name, student_id))  # \n is new line   \t is tab key





