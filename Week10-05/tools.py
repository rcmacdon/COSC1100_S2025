# -----------------------------------------------
# Title:    My Tools Library for Python Console
# Author:   Clint MacDonald
# Date:     July 17, 2025
# Purpose:  A set of tools to be reused in our console apps
# Modified by:
# Modification Date: 
# ----------------------------------------------
# 
#  
'''
Note that this file does use print statements in the functions meaning it is locked 
to the console.  If you want to use these functions in a GUI, you will need to modify the functions to return values instead of printing them.
'''

#region IMPORTS
import random
#endregion

#region USER INPUT FUNCTIONS

def getString(prompt: str):
    '''Obtains a string from the user'''
    return input(prompt).strip()

def getStringLength(prompt: str, minLen: int, maxLen, int):
    '''Obtains a string from the user with length inside the given range'''
    isValid = False
    while not isValid:
        userString = input(prompt).strip()
        # validate the length of the string
        if minLen <= len(userString) <= maxLen: return userString
    
def getInt(prompt: str):
    '''Get an integer from the user'''
    isValid = False
    while not isValid:
        try:
            return int(input(prompt).strip())
        except ValueError as v:
            pass

def getIntRange(prompt: str, min: int, max: int):
    '''Get an integer from the user within specified range'''
    isValid = False
    while not isValid:
        try:
            my_int = int(input(prompt).strip())
            if min <= my_int <= max: return my_int
        except ValueError as v:
            pass

def getFloat(prompt: str):
    '''get a valid float from the user'''
    is_valid = False
    while not is_valid:
        try:
            return float(input(prompt).strip())
           
        except ValueError as v:
            pass

def getFloatRange(prompt: str, min: float, max: float):
    '''Get a float from the user within a specified range'''
    is_valid = False
    while not is_valid:
        try:
            num= float(input(prompt).strip())
            if min <= num <= max: return num

        except ValueError as v:
            pass


#endregion

#region RANDOM NUMBER GENERATIONS
def getRandIntRange(min: int, max: int):
    '''generate a random integer within the specified range'''
    return random.randint(min, max)

def getRandFloatRange(min: float, max: float, numDec: int):
    '''generate a random float within the specified range'''
    rnd = random.randint(min * (10 ** numDec), max * (10 ** numDec)) / (10**numDec)
    pass


#endregion

