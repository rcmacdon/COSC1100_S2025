# -------------------------
# COSC1100 - Week 8 Sample 2
# Clint MacDonald
# July 4, 2025
# Golf Simulator to learn to use arrays in practice
# -------------------------

#region IMPORTS

#endregion

#region DECLARATIONS

#region CONSTANTS
NUM_HOLES = 9
PAR_SCORES = [36, 4, 3, 5, 4, 3, 5, 5, 3, 4]
MAXIMUM_STROKES = 12
#endregion

#region LOCAL VARIABLES
player_name = ''
shots_taken = [0]

welcome_message = 'Welcome to the Deer Ridge Golf Scorecard!'
instructions = '''
After entering your name, 
you will enter the stroke count for each hole you play, one at a time!  

Your score must be entered as an integer!
'''
#endregion

#endregion

#region INFORMATION
print(welcome_message)
print(instructions)
#endregion

#region Gather basic Information
player_name = input("Please enter your name: ").strip()

#endregion

play_again = True
while play_again:
    current_hole = 1

    #region play round of golf

    # loop to get scores for each hole played
    while current_hole <= NUM_HOLES:
        # retrieve the score for this hole
        try:
            temp_score = int(input("Enter your score for hole %i: " % current_hole))

            if not 0 < temp_score <= MAXIMUM_STROKES:
                raise ValueError
            
            shots_taken.append(temp_score)
            shots_taken[0] = sum(shots_taken) - shots_taken[0]

        except ValueError as v:
            print("You did not enter a valid golf score! try again!")
            continue

        # compare to par for each hole and give feedback
        score = shots_taken[current_hole] - PAR_SCORES[current_hole]
        result = ''
        if score < -2:
            result = "Albatross!"
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

        print("You got a score of %i - %s" % (score, result))

        # increment hole number
        current_hole += 1

    #endregion

    #region Output of some stats

    # calculate total strokes
    print("Your total strokes was: %i" % (shots_taken[0]))
    # calculate total score
    print("Your final score was: %i" % (shots_taken[0] - PAR_SCORES[0]))
    # give feedback
    if shots_taken[0] - PAR_SCORES[0] < 0:
        print("Congrats you were under par!")
    else:
        print("Keep improving and you will beat par one day!")

    # reset
    shots_taken.clear()
    shots_taken.append(0)

    play_again = input("Do you want to play again (y/n)?")[0].strip().lower() == 'y'
    #endregion

# play again?

