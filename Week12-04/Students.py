# ----------------------------------------
# setting up lists inside lists
# Clint MacDonald
# July 31, 2025
# simulating a 2D array
# ----------------------------------------

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

for stud in students:
    print("-"*60)
    print("%15s: %s" % ("First Name", stud[FIRST_NAME]))
    print("%15s: %s" % ("Last Name", stud[LAST_NAME]))
    print("%15s: %s" % ("Date of Birth", stud[BIRTHDATE]))
    print("%15s: %s" % ("Course Code", stud[COURSE_CODE]))
    print("%15s: %i" % ("Grade", stud[GRADE]))
    print("%15s: %i" % ("Section", stud[SECTION_NUMBER]))


print("-"*60)

print(students[1][4])
print(students[1][GRADE])