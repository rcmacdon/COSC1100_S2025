# ---------------------------------------
# Title:    Iteration Basics
# Author:   Clint MacDonald
# Date:     May 26, 2025
# Purpose:  Learning the Basics of Loops
# ---------------------------------------

# In mainstream programming there are 4 types of loops..
# 1. For Loop
# 2. While Loop
# 3. Do While Loop (Loop Until)
# 4. For Each Loop

# In Python, the Do While (Loop Until) technically does not exist.

# --------------------------------
# For Loop
# used to iterate when we know exactly how many iterations we want
print('-'*60)
print('Basic For Loop')

# in java
# for (int i; i < 5; i++) {
#    commands
# }

for i in range(5):
    print(i)
    print('in the loop')
    # end of the loop
print('not in the loop')

    # doing a loop where i = 0 on the first loop
    # each time through the loop, i will increment by 1

# 2. While Loop
# used when you want to loop until some condition is met
print('-'*60)
print('While Loop')

num_students = 12
while num_students > 0:
    print('Good-bye, there are %i students left' % num_students)
    num_students = num_students - 1
    # num_students -= 1
print('There are no students left!')

# 3. Do While .....
# other languages
#   loop {
#       command block
#   } until (condition)
i = 0
while True:  # UNACCEPTABLE
    print(i)
    i += 2
    if i >= 1000:
        break   # UNACCEPTABLE (except search engines)
print ('We are done the loop')

# Rewrite to make this acceptable
i = 0
doContinue = True
while doContinue:  
    print(i)
    i += 2
    if i >= 1000:
        doContinue = False   
print ('We are done the loop')

# For Each Loop
# We do not know how many there are, but we want to do ALL of them
print('-'*60)
print('Basic For Each Loop')

for letter in "Hello World!":
    print(letter)

# the following is an ERROR and hard to use
# myString = "Hello World!"
# for i in range(len(myString)+1):
#     print(myString[i])

# -----------------------------------------
# Various variants of loops
#
print ('-'*60)
print('For loop with start and stop')
# For loop with a start and stop 
for i in range(5, 10):
    print(i)
    print('in the loop')
    # end of the loop
print('not in the loop')


print ('-'*60)
print('For loop with start, stop, and a step')
for i in range(7, 15, 3):
    print(i)
    print('in the loop')
    # end of the loop
print('not in the loop')


print ('-'*60)
print('For loop with start, stop, and a step (Negative)')
for i in range(15, 7, -3):
    print(i)
    print('in the loop')
    # end of the loop
print('not in the loop')

