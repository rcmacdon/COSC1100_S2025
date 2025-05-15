# ----------------------------------
# Title: COSC1100 - Learning Control Statements
# Author: Clint MacDonald
# Date: May 15, 2025
# Purpose: Learning conditional statements and Code Blocks
# ----------------------------------

# Display the menu!
menu = '''-----------------------
MENU
-----------------------
1 - Say Hello World!
2 - Say Who Am I!
3 - Exit
Make your choice (1-3):
'''

# Prompt user for their choice
# Receive and store the choice
choice = input(menu)

# Based on which choice, do something different
if choice == "1":
    print("You chose 1")
    print("Hello World!")
elif choice == "2":
    print("You chose 2")
    print("Who Am I")
elif choice == "3":
    print("Good-bye!")
    exit()
else:
    print("Dummy, you entered an invalid value!")
    print("Good-bye!")
    exit()
    # end of else
print("You made it through the menu!")
exit()

