# --------------------------------
# COSC1100 - Week 9 Function Example
# Clint MacDonald
# July 11, 2025
# a tool for profs to handle student grades
# --------------------------------

#region IMPORTS
#endregion

#region DECLARATIONS
WELCOME_MESSAGE = '''Welcome to the grade calculator!'''
MAIN_MENU = '''Main Menu
----------------------
1. Add a student grade
2. Find a student grade
3. Show statistics
4. Show all grades
5. exit
'''
MINIMUM_GRADE = 0.0
MAXIMUM_GRADE = 100.0
students = []
grades = []
#endregion

#region FUNCTIONS
#region Input Functions 
def getIntInRange(prompt, min: int, max: int):
    '''Get an integer from the user within the given range!'''
    is_valid = False
    while not is_valid:
        try:
            tempNum = int(input(prompt))

            if not min <= tempNum <= max:
                print("Must be between %i and %i" % (min, max))
                continue

            return tempNum
        except ValueError as v:
            print("Invalid input, must be an integer!")

def getFloatInRange(prompt, min, max):
    '''Get an float from the user within the given range!'''
    is_valid = False
    while not is_valid:
        try:
            tempNum = float(input(prompt))

            if not min <= tempNum <= max:
                print("Must be between %.2f and %.2f" % (min, max))
                continue

            return tempNum
        except ValueError as v:
            print("Invalid input, must be a number!")

def getString(prompt):
    '''prompt the user to enter a string!'''
    is_valid = False
    while not is_valid:
        tempName = input(prompt)

        if len(tempName.strip()) > 1:
            return tempName.strip()
#endregion

#region Custom Functions
def addStudent():
    # get students name
    students.append(getString("Enter the students name: "))
    # get students grade
    grades.append(getFloatInRange("Enter the students grade: ", MINIMUM_GRADE, MAXIMUM_GRADE))

def findStudent():
    # get student name
    student_name = getString("Enter the student's name: ")
    # check if student exists
    if student_name in students:
        # get the associated index number
        index = students.index(student_name)
        # display grade
        print("%s's grade is %.2f" % (student_name, grades[index]))

    else:
        print("That student could not be found!")


def showAllGrades():
    for i in range(0, len(students)):
        print("%2i: %12s - %6.2f" % (i+1, students[i], grades[i]))

def showStats():
    # show number of students
    print("Number of students: %i" % len(students))
    try:
        # show minimum grade
        print("Minimum grade: %.2f" % min(grades))
        # show maximum grade
        print("Maximum grade: %.2f" % max(grades))
        # show average grade
    
        print("Average Grade: %.2f" % (sumGrades()/len(grades)))
    except:
        print("There are no students to do calculations!")

def sumGrades():
    sum = 0
    for grade in grades:
        sum += grade

    return sum

#endregion


#endregion

#region MAIN PROGRAM

# greet the user
print(WELCOME_MESSAGE)

choice = 0
while not choice == 5:
    # show menu
    print(MAIN_MENU)
    # get choice from the user
    choice = getIntInRange("Enter your choice (1-5)", 1, 5)
    # process the choice
    if choice == 1:    addStudent()
    elif choice == 2:  findStudent()
    elif choice == 3:  showStats()
    elif choice == 4:  showAllGrades()

    input("-- press enter to continue --")

# exit the program
print("Good-bye")
exit()

#endregion