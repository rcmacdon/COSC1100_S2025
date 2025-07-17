# --------------------------------
# Library of tools that I can use repeatedly in different applications.
# Author: Clint MacDonald
# Date: July 17, 2025
# Modified By: 
# Date Modified: 
# ---------------------------------

'''
DO NOT USE PRINT in a library
'''

#region IMPORTS
import random
#endregion

#region USER INPUT FUNCTIONS

def getString(prompt: str):
    '''Get a string from the user!'''
    return input(prompt).strip()

def getStringLength(prompt: str, minLen: int, maxLen: int):
    '''Obtains a string from the user within a specified length'''
    is_valid = False
    while not is_valid:
        userString = input(prompt).strip()
        if minLen <= len(userString) <= maxLen: return userString

def getInt(prompt: str):
    '''Get an integer from the user'''
    isValid = False
    while not isValid:
        try:
            return int(input(prompt).strip())
        except ValueError as v:
            pass

def getIntBelow(prompt: str, max: int):
    '''Get an integer from the user below a given value'''
    isValid = False
    while not isValid:
        try:
            num = int(input(prompt).strip())
            if num <= max: return num

        except ValueError as v:
            pass

def getIntRange(prompt: str, min: int, max: int):
    '''Get an integer from the user withing a given range'''
    isValid = False
    while not isValid:
        try:
            num = int(input(prompt).strip())
            if min <= num <= max: return num
            
        except ValueError as v:
            pass

def getFloat(prompt: str):
    '''Get an float from the user'''
    isValid = False
    while not isValid:
        try:
            return float(input(prompt).strip())
        except ValueError as v:
            pass

def getFloatRange(prompt: str, min: float, max: float):
    '''Get an float from the user withing a given range'''
    isValid = False
    while not isValid:
        try:
            num = float(input(prompt).strip())
            #if min <= num <= max: return num
            if (num >= min and num <= max): return num
            
        except ValueError as v:
            pass

#endregion

#region RANDOM NUMBER GENERATION

def getRandIntRange(min: int, max: int):
    '''Returns a random integer within the given range'''
    return random.randint(min,max)

def getRandFloat(min: float, max: float, numDec: int):
    '''Returns a random float within a given range'''
    #return random.randint(min * (10**numDec), max*(10**numDec)) / (10**numDec)
    return getRandIntRange(min * (10**numDec), max*(10**numDec)) / (10**numDec)

#endregion


