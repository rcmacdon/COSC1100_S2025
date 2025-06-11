# -------------------------------------------- 
# Title:        Guess the Number Game
# Author:       Clint MacDonald
# Date:         May 29, 2025
# Purpose:      To put nested looping into practice
# -------------------------------------------
import random

# Set game parameters
MIN_NUMBER = 1
MAX_NUMBER = 100

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

# ------------  The Game  -----------------
play_again = True
while play_again:

    # Generate Random Number
    game_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    # Set/Reset guess counter to 0
    guesses = 0

    # --------  get a guess  -----------------
    prompt = ("I though of a number between %i and %i.\nYou have to guess it!" % (MIN_NUMBER, MAX_NUMBER))
    print(prompt)
    
    guess_again = True
    while guess_again:
        # prompt user for guess, wait for guess, and store in a variant
        guess = input("Enter your guess: ")

        # Check if the guess is appropriate (number and in range)
        # check if valid # if no, get another guess
        if not guess.isdigit():
            print("Invalid Guess, try again!")
            continue
        
        guess = int(guess)
        # check if the number is within a valid range
        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print("Invalid number range, try again!")
            continue
        
        # if yes, increment guess count and then compare number
        guesses += 1

        # if too high or too low, msg user and get another guess!
        if guess > game_number:
            print("too high! Try Again!")
            continue
        elif guess < game_number:
            print("too low! Try Again!")
            continue

        # if correct guess - msg user with congrats and num guesses
        guess_again = False
        print('Congrats, you got it in %i guesses!' % guesses)
        print('-'*60)

        # ----------  END OF GUESSING LOOP

    # Ask user if they want to play again?
    play_again = input("Do you want to play again (y or n)?").lower().strip()[0] == "y"

    # ------------ END OF THE PLAYING LOOP

# Exit program
print("Good-bye")
exit()
