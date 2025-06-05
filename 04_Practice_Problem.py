# -----------------------------
# Practice Problem Week 5
# Clint MacDonald
# June 5, 2025
# -----------------------------

MIN_AGE = 19
MAX_AGE = 120
SENIOR_CITIZEN = 65
DISCOUNT_AMOUNT = "10%"

do_another = True
while do_another:
    
    try:
        age_entered = input("Enter your age! (q to quit)")

        # check if quitting
        if age_entered.lower() == 'q':
            do_another = False
            continue

        # convert to an integer
        age_entered = int(age_entered)

        # check if within range
        if not MIN_AGE <= age_entered <= MAX_AGE:
            raise Exception("Age entered was not within a valid range!")
        
        # successful!  message user
        print("Thank-you for entering a valid age!")

        # offer discount to seniors
        if age_entered >= SENIOR_CITIZEN:
            print("Congrats, you get a discount of: %s" % DISCOUNT_AMOUNT)

    # exception handling
    except ValueError as v:
        print("That entry was not a number!")
    except Exception as e:
        print(e)

# end of program!
print("Good-bye")
exit()