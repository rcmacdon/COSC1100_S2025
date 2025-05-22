# -----------------------------------
# TITLE:    Week 3 - Temperature Converter
# AUTHOR:   Clint MacDonald
# DATE:     May 22, 2025
# PURPOSE:  Full application for the first time
# -----------------------------------

# ASSUMPTION: the user will always type info in correctly

# Concept: We will ask the user for a temperature that includes the units
#          We will then convert the temperature to the OTHER unit.
#          User input will look like ##.#C or ##.#F.

# declarations
TEMPERATURE_CONVERSION_RATIO = 9.0 / 5.0
TEMPERATURE_CONVERSION_CONSTANT = 32

# Information
# greet the user
print('--------------------------------------')
print('Welcome to Clint\'s temperature converter!')

# Input
# prompt for Input
# wait for the users input and store in memory (variable)
user_input = input('Enter your temperature. including units (##.#C or ##.#F): ')

# Process
# separate the number from the units
temperature_value = user_input[:-1]
temperature_unit = user_input[-1]

# # temp code
# print(temperature_value)
# print(temperature_unit)

# determine what unit was entered
if temperature_unit == 'F':
    # Calculate new temperature and unit
    new_temperature = (float(temperature_value)-TEMPERATURE_CONVERSION_CONSTANT) / TEMPERATURE_CONVERSION_RATIO
    new_unit = 'C'
elif temperature_unit == 'C':
    # Calculate new temperature and unit
    new_temperature = TEMPERATURE_CONVERSION_RATIO * float(temperature_value) + TEMPERATURE_CONVERSION_CONSTANT
    new_unit = 'F'
else:
    print("Enter it as described dummy!!!  Good-bye!")
    exit()

# Output
# Output the results to the user
# including the correct NEW unit
print('The new temperature is %.2f %s' % (new_temperature, new_unit) )

print('--------------------------------------')