# -----------------------------------------------
# Title:    DnD Dice Rolling App
# Author:   Clint MacDonald
# Date:     July 17, 2025
# Purpose:  A tool to roll combinations of dice for DnD
# ----------------------------------------------

#region IMPORTS
import tools
#endregion

#region CONSTANTS and GLOBAL VARIABLES
num_dice = 0
WELCOME_MESSAGE = 'how many dice and how many sides?'
ALLOWABLE_SIDES = [4,6,8,10,12,20]
#endregion

#region custom FUNCTIONS
def get_number_of_sides():
    '''Determine the number of sided dice within a specific list of sides'''
    isValid = False
    while not isValid:
        num_sides = tools.getIntRange("How many sides (" + str(ALLOWABLE_SIDES) + ")? ", 4, 20)
        #isValid = num_sides in ALLOWABLE_SIDES
        if num_sides in ALLOWABLE_SIDES:
            isValid = True
    return num_sides

def roll_dice(numDice, numSides):
    '''Roll n dice of m sides to get a total roll'''
    total = 0
    for dice in range(0,numDice):
        total += tools.getIntRange(1,numSides)
    return total
#endregion

#region Main Program
print(WELCOME_MESSAGE)
num_dice = tools.getInt("How many dice are you rolling? ")
num_sides = get_number_of_sides()
total = roll_dice(num_dice, num_sides)
print("You rolled a " + str(total))


#endregion
