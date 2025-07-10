# -----------------------------------
# COSC1100 - Week 9 demo 2
# Clint MacDonald
# July 10, 2025
# Redoing the Guess the number game using functions and modularity
# -----------------------------------
# 
#region Design Concepts 
#  IDFIIPO
# Imports
# Declaration
# Functions
# Information
# Input
# Processing
# Output
#endregion

#region IMPORTS
import random
#endregion

#region DECLARATIONS
theNumber = 0
minNumber = 0
maxNumber = 100
#endregion

#region FUNCTIONS
def getString(prompt):
    '''prompt the user to enter a string!'''
    is_valid = False
    while not is_valid:
        tempName = input(prompt)

        if len(tempName.strip()) > 1:
            return tempName.strip()

def getInt(prompt):
    '''prompt the user for an integer'''
    is_valid = False
    while not is_valid:

        try:
            return int(input(prompt))
        except ValueError as v:
            print("Invalid input, must be an integer!")

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

def getRandomIntInRange(min: int, max: int):
    '''Function the returns a random integer within the specified range.'''
    return random.randint(min, max)




#endregion

#region INFORMATION

#endregion


#region Main Program

playerName = getString("Please tell me your name: ")
minNumber = getInt("Please enter the lower bound: ")
maxNumber = getIntInRange("Please enter the upper bound", minNumber + 1, 1000)
theNumber = getRandomIntInRange(minNumber, maxNumber)

do_guess = True
while do_guess:
    guess = getIntInRange("Enter your guess: ", minNumber, maxNumber)

    if guess > theNumber:
        print("Too High")
    elif guess < theNumber: 
        print("Too Low")
    else:
        print("Congrats!")
        do_guess = False

print("Good-bye")
exit()


#endregion