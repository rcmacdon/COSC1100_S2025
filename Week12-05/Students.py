# ---------------------------------------
# Setting up a list inside a list
# Clint MacDonald
# July 29, 2025
# simulating a 2D Array
# ---------------------------------------

FIRST_NAME = 0
LAST_NAME = 1
BIRTHDATE = 2
COURSE_CODE = 3
GRADE = 4
SECTION_NUMBER = 5

students = []

student = ["Clint", "MacDonald", "05/16/1972", "COSC1100", 67, 5]
students.append(student)
student = ["Sally", "Smothers", "08/12/1990", "SYD366", 89, 2]
students.append(student)

for s in students:
    print("-"*60)
    print("%15s: %s" % ("First Name", s[FIRST_NAME]))
    print("%15s: %s" % ("Last Name", s[LAST_NAME]))
    print("%15s: %s" % ("Birthdate", s[BIRTHDATE]))
    print("%15s: %s" % ("Course Code", s[COURSE_CODE]))
    print("%15s: %s" % ("Grade", s[GRADE]))
    print("%15s: %s" % ("Section", s[SECTION_NUMBER]))

print("-"*60)

print(students[1][4])
print(students[1][GRADE])
