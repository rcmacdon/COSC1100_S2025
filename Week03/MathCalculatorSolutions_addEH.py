# -------------------------------------------
# TITLE:    IP2 Calculator
# AUTHOR:   Clint MacDonald
# DATE:     May 2025
# PURPOSE:  This program that calculates single digit integer math
# -------------------------------------------

# greet the user and provide basic instructions
print("-"*60)
print(
"""Welcome to the IP2 Calculator by Clint

This program will calculate single digit integer math.  
The user will input an integer followed by an operator (+, -, *, /) 
followed by another integer #O#.

example: 5*4 will do 5 x 4 = 20""")

loop_again = True
while loop_again:

    print("-"*60)

    # prompt the user, get the input, and store it in a temp variable
    user_input = input("Enter your math problem (#O#): ")

    # split the user input into 3 separate variables
    # check if the length of the user input was 3
    # if len(user_input) != 3:
    #     print("Invalid input. Please enter single digit integers only.  Your entire input should be 3 characters long.")
    #     exit()

    # split the user input into 3 separate variables

    # need exception handling here
    try:
        # --------------------------
        num1 = user_input[0]
        operator = user_input[1]
        num2 = user_input[2]
        # --------------------------
    except IndexError:
        print("Your input must be of length 3")
        continue
        
    # convert the strings to integers
    #if num1.isdigit() and num2.isdigit():

    # need exception handling here
    try:
        # -------------------------------
        num1 = int(num1)
        num2 = int(num2)
        # -------------------------------
    except ValueError:
        print("Input was not of type number!")
        continue

    # check which operator the user input and perform the appropriate math calculation
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    elif operator == "/":

        # need exception handling here
        try:
            # -------------------------------
            answer = num1 / num2
            # -------------------------------
        except ZeroDivisionError:
            print("You cannot divide by zero!")
            continue

    else: # the operator entered was not +, -, *, or /
        print("Invalid operator. Please enter +, -, *, or /")
        continue

    # print the answer
    print("%i %s %i = %.2f" % (num1, operator, num2, answer))
    #print(f"{num1} {operator} {num2} = {answer}")

    print('-'*60)
    user_want_to_do_again = input("Do you want to do another one? (y or n)")
    try:
        user_want_to_do_again = user_want_to_do_again[0]
    except:
        print("Assuming you wanted to leave!")
        loop_again = False
        
    user_want_to_do_again = user_want_to_do_again.lower()
    if not user_want_to_do_again == "y":
        loop_again = False

print('Good-bye')
exit()