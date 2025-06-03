# -----------------------------
# Class Exercise 2 - Multiplication Table
# Clint MacDonald
# May 30, 2025
# -----------------------------

# Declarations
MIN_NUMBER = 1
MAX_NUMBER = 25

# Information
string_welcome = '''
------------------------------------------------
Welcome to the multiplication table application!
------------------------------------------------
'''

print(string_welcome)

do_another = True
while do_another:

    # Input
    user_input = input(("Enter a number between %i and %i (q to quit)" % (MIN_NUMBER, MAX_NUMBER)))

    # check if the quit
    if user_input[0].lower() == 'q':
        do_another = False
        continue

    # check if input is numeric
    if not user_input.isnumeric():
        print("you must enter an integer!")
        continue

    # convert to a number
    number = int(user_input)

    # check if input was within correct range
    if not MIN_NUMBER <= number <= MAX_NUMBER:
        print("the number must be between %i and %i" % (MIN_NUMBER, MAX_NUMBER))
        continue
    
    # Print Header Row
    string_line = "    "
    for i in range(1, number + 1):
        string_line = ('%s%4i' % (string_line, i))
    print(string_line) 
    print(' ---'*(number+1))

    # loop rows
    for row in range(1,number+1):

        row_string = str('%2i |' % row )

        # loop columns building the string
        for column in range(1,number+1):
            row_string = ('%s%4i' % (row_string, row*column))

        print(row_string)

    do_another = input("Do you want to do another one? (y or n)").strip().lower() == 'y'

print("Good-bye")
input("\npress enter to exit!")
exit()