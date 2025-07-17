# ------------------------------
# Dice rolling program
# Clint MacDonald
# July 17, 2025
# to learn to use our tools library
# ------------------------------

#region IMPORTS
import tools
#endregion

#region CONSTANTS AND VARIABLES
MAX_DICE = 20
ALLOWED_DICE = [4,6,8,10,12,20]
WELCOME_MESSAGE = 'Welcome to the dice rolling simulator!'
#endregion

#region Custom Functions
def getDiceType(prompt: str):
    '''Get type of dice from user within predetermined list'''
    is_valid = False
    while not is_valid:
        num_sides = tools.getIntRange(prompt, min(ALLOWED_DICE), max(ALLOWED_DICE))
        if num_sides in ALLOWED_DICE: return num_sides

def roll_dice(numDice: int, numSides: int):
    '''roll the number of dice specified returning the total'''
    total = 0
    for dice in range(numDice):
        total += tools.getRandIntRange(1, numSides)
    return total

#endregion

#region Main Program
print(WELCOME_MESSAGE)
# ask user how many dice
num_dice = tools.getIntRange("How many dice are you rolling? ", 1, MAX_DICE)
# ask the user what kind of dice
num_sides = getDiceType("What kind of dice are you rolling (" + str(ALLOWED_DICE) + ") ? " )
# randomly roll the dice adding up total
total = roll_dice(num_dice, num_sides)
# print the output
print("You rolled a %i" % total)

exit()
#endregion