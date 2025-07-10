# ----------------------------
# COSC1100- Week 9 Guess the Number
# Clint MacDonald
# July 10, 2025
# Showing hwo to integrate functions into programs
# ----------------------------

# IDFIIPO
#region Imports
import random
#endregion

#region Declarations
theNumber = 0
minNumber = 0
maxNumber = 100
#endregion

#region Functions
def getStringFromUser(prompt):
    return input(prompt).strip()

def getPositiveIntegerFromUser(prompt):
    try:
        return int(input(prompt))
    except ValueError as v:
        return -1
    
def getPositiveIntegerInRangeFromUser(prompt, minimum, maximum):
    is_valid = False
    while not is_valid:
        try:
            num= int(input(prompt).strip())

            if not minimum <= num <= maximum:
                print("That number was not in the right range")
                raise ValueError
            
            is_valid = True
        except ValueError as v:
            print("Invalid input")

    return num


def getRandomInt(min, max):
    return random.randint(min, max)

#endregion

#region Information

#endregion


#region Main Program
print('-'*40)

playerName = getStringFromUser("Please enter your name: ")
minNumber = getPositiveIntegerFromUser("Please enter the lower bound: ")
maxNumber = getPositiveIntegerFromUser("Please enter the upper bound: ")
theNumber = getRandomInt(minNumber, maxNumber)

do_guess = True
while do_guess:

    guess = getPositiveIntegerInRangeFromUser(minNumber, maxNumber)
    if guess > theNumber:
        print("too High")
    elif guess < theNumber:
        print("Too Low")
    else:
        print("Congrats you got it")
        do_guess = False

print("Good-bye")
exit()

#endregion


