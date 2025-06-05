# -------------------------------------------- 
# Title:        Guess the Number Game
# Author:       Clint MacDonald
# Date:         May 29, 2025
# Purpose:      To put nested looping into practice
# Revised:      June 5, 2025 by author
# -------------------------------------------
import random

# Set game parameters
MIN_NUMBER = 1
MAX_NUMBER_EASY = 10
MAX_NUMBER_MEDIUM = 100
MAX_NUMBER_HARD = 1000
max_number = MAX_NUMBER_MEDIUM

# Welcome the User
welcome_message = '''
---------------------------------------------------
Welcome the the Guess the number game!
You will guess a number and the computer will
tell you if it was too low, too high, or correct.
See how few guesses you can get it right in!
--------------------------------------------------- 
'''
print(welcome_message)

# Difficulty choice selection
difficulty_menu = '''
      What difficulty do you want to play at?
      1 - Easy
      2 - Medium
      3 - Hard
      q - quit
      Enter your choice (1-3): 
      '''

# loop to decide difficulty level
play_game = True
while play_game:

    user_input = input(difficulty_menu)

    # processing the user input
    if      user_input == "1":      max_number = MAX_NUMBER_EASY
    elif    user_input == "2":      max_number = MAX_NUMBER_MEDIUM
    elif    user_input == "3":      max_number = MAX_NUMBER_HARD
    elif    user_input.lower() == "q":
        play_game = False
        continue 
    else:
        print("invalid choice!")
        continue

    # ------------  The Game  -----------------
    play_again = True
    while play_again:

        # Generate Random Number
        game_number = random.randint(MIN_NUMBER, max_number)

        # Set/Reset guess counter to 0
        guesses = 0

        # --------  get a guess  -----------------
        prompt = ("I though of a number between %i and %i.\nYou have to guess it!" % (MIN_NUMBER, max_number))
        print(prompt)
        
        guess_again = True
        while guess_again:
            # prompt user for guess, wait for guess, and store in a variant
            guess = input(("Enter your guess (%i - %i): " % (MIN_NUMBER, max_number)))

            # Check if the guess is appropriate (number and in range)
            # check if valid # if no, get another guess
            # if not guess.isdigit():
            #     print("Invalid Guess, try again!")
            #     continue
            
            try:
                guess = int(guess)
                # check if the number is within a valid range
                if not MIN_NUMBER <= guess <= max_number:
                    raise Exception(("Invalid number range, the number needs to be between %i and %i, try again!" % (MIN_NUMBER, max_number)))

                # if yes, increment guess count and then compare number
                guesses += 1
            except ValueError as v:
                print("Invalid Guess!  Please try again!")
                continue
            except Exception as e:
                print(e)
                continue

            # if too high or too low, msg user and get another guess!
            message_string = ""
            if guess > game_number:     
                message_string = "too high! Try Again!"
            elif guess < game_number:   
                message_string = "too low! Try Again!"
            else:                       
                message_string = 'Congrats, you got it in %i guesses!' % guesses

                # if correct guess - msg user with congrats and num guesses
                guess_again = False
                print('Congrats, you got it in %i guesses!' % guesses)
                print('-'*60)

            # ----------  END OF GUESSING LOOP

        # Ask user if they want to play again?
        play_again = input("Do you want to play again (y or n)?")[0].lower().strip() == "y"
        # ------------ END OF THE PLAYING LOOP

# Exit program
print("Good-bye")
exit()
