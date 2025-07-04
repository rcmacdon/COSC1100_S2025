# --------------------- 
# COSC1100 - Week 8 Arrays Sample Prog
# Clint MacDonald
# July 4, 2025
# Using Arrays in a program
#
# Golf Simulator for 1 player at a constant golf course
# we will greet by name and produce some basic stats at the end
# We will allow the player to play again! 
# ---------------------

#region IMPORTS
#endregion

#region DECLARATIONS

#region CONSTANTS
MINIMUM_STROKES = 1
MAXIMUM_STROKES = 12
NUM_HOLES = 9
PAR_SCORES = [ 36, 4, 3, 5, 4, 5, 3, 5, 3, 4 ] # index 0 is used for the total
#endregion

#region VARIABLES
number_strokes = [ 0 ]
player_name = ''
play_again = True

welcome_message = 'Welcome to the Deer Ridge Golf Simulator!'
instructions = '''
After entering your name, you will enter the stroke count for each hole in succession.  Each score must be a whole number between %i and %i.
''' % (MINIMUM_STROKES, MAXIMUM_STROKES)
#endregion


#endregion

#region INFORMATION

# greeting
print(welcome_message)
# instructions
print(instructions)
#endregion

#region Gather Basic Information
player_name = input("Please enter your name! ").strip()
#endregion

#region Play the Game
while play_again:

    current_hole = 1
    number_strokes.clear()
    number_strokes.append(0)

    # loop through each hole (until all holes are done) to get the player stroke count
    while current_hole <= NUM_HOLES:

        try:
            # get the the score from the player for the current hole
            temp_score = int(input("Enter your score for hole %i: " % current_hole))

            # validate the score
            if not MINIMUM_STROKES <= temp_score <= MAXIMUM_STROKES:
                raise ValueError
            
            # store the score
            number_strokes.append(temp_score)
            # or -> number_strokes[current_hole] = temp_score

        except ValueError as v:
            print("You did not enter a valid golf score! try again!")
            continue

        # compare the score to par, and give some feedback
        score = number_strokes[current_hole] - PAR_SCORES[current_hole]
        result = ''
        if score <= -3:
            result = "Albatross"
        elif score == -2:
            result = "Eagle"
        elif score == -1:
            result = "Birdie"
        elif score == 0:
            result = "Par"
        elif score == 1:
            result = "Bogie"
        elif score == 2:
            result = "Double Bogie"
        elif score == 3:
            result = "Triple Bogie"
        else:
            result = "Other"

        print("You got a %i - %s!" % (score, result))
        number_strokes[0] = sum(number_strokes) - number_strokes[0]

        # increment the hole number
        current_hole += 1

        #endregion

    #region Output to the User

    # final score
    print("Your total strokes was %i" % number_strokes[0])
    print("You final score was %i" % (number_strokes[0] - PAR_SCORES[0]))

    # average score per hole
    print("You average score per hole was %.2f" % (number_strokes[0] / NUM_HOLES))
    # verbal feedback on overall result
    if (number_strokes[0] - PAR_SCORES[0]) < 0:
        print("Congrats you got under par overall!")
    else:
        print("You'll get under par one day!!!!")

    #endregion

    # play again?
    play_again = input("Do you want to play again (y/n)?").strip().lower()[0] == 'y'

print('Good-bye')
exit()