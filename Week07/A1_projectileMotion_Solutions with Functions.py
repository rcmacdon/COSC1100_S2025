# ------------------------------------
# Title:    Projectile Motion Calculations
# Author:   Clint MacDonald
# Date:     Feb. 4, 2025
# Purpose:  To calculate the time it takes for a projectile
#           to hit the ground mapping it's location each time interval.
# ------------------------------------

#region IMPORTS
import math, random
#endregion

#region CONSTANTS and GLOBAL VARIABLES
# ------------------------------------
# CONSTANTS
GRAVITY = -9.81  # acceleration due to gravity (m/s^2)
INITIAL_VELOCITY = 175.0  # initial velocity of the projectile (m/s)
PI = 3.14159
MIN_START_DISTANCE = 250
MAX_START_DISTANCE = 4000
MIN_SHOT_ANGLE = 0.0
MAX_SHOT_ANGLE = 90.0
HIT_DISTANCE = 5.0
SELF_DESTRUCT_DISTANCE = 5.0
TIME_INTERVAL = 2.0

WELCOME_MESSAGE = "Welcome to the Canon Ball Calculator!"
MAIN_MENU = """------------------------------------
Main Menu
------------------------------------
1. Easy Mode - stationary tank and target
2. Hard Mode - moving tank and stationary target
3. Extreme Mode - moving tank and moving target
q. Quit"""


targetDistance = 0
num_shots = 0
game_win = False

initial_velocity_x = 0
initial_velocity_y = 0
#endregion

#region FUNCTIONS

#region Input Functions
def getString(prompt):
    return input(prompt).strip()

def getFloatInRange(prompt, min, max):
    '''Get an float from the user within the given range!'''
    is_valid = False
    while not is_valid:
        try:
            tempNum = float(input(prompt))

            if not min <= tempNum <= max:
                print("Must be between %.2f and %.2f" % (min, max))
                continue

            return tempNum
        except ValueError as v:
            print("Invalid input, must be a number!")

#endregion

#region Custom Functions
def playGame():
    # get random distance
    playGame = True
    while playGame:
        initializeGame()
        playRounds()

def initializeGame():
    targetDistance = float(random.randint(MIN_START_DISTANCE*10, MAX_START_DISTANCE*10)) / 10.0
    num_shots = 0
    game_win = False

def playRounds():
    shootAgain = True
    while shootAgain: 
        print('-'*40,"\nTarget distance is {:.1f} meters.".format(targetDistance))
        angle = getFloatInRange("Enter your shot angle in degrees: ", MIN_SHOT_ANGLE, MIN_SHOT_ANGLE)
        calculateInitialVelocities(angle)
        displayCoords()
        determineResults()
        

def calculateInitialVelocities(angle:float):
    initial_velocity_x = INITIAL_VELOCITY * math.cos(math.radians(angle))
    initial_velocity_y = INITIAL_VELOCITY * math.sin(math.radians(angle))

def displayCoords():
    # Time iterations
    time = 0
    position_x = 0
    position_y = 0

    # Manually output the initial time and position
    print("Initial time and position: {:.2f} seconds, x: {:.2f} meters, y: {:.2f} meters".format(time, position_x, position_y))

    while position_y >= 0:
        time = time + TIME_INTERVAL

        position_x = initial_velocity_x * time
        position_y = initial_velocity_y * time + 0.5 * GRAVITY * time ** 2

        # output starting height and time
        print("Time {:.2f} seconds, x = {:.2f}m, y = {:.2f}m.".format(time, position_x, position_y))

    # --- end time interval loop ---

def displayCalculatedDistances():
    # Calculate the exact time it takes for the projectile to hit the ground
    # time_to_hit_ground = (initial_velocity_y + math.sqrt(initial_velocity_y ** 2 - 2 * GRAVITY * 0)) / GRAVITY
    time_to_hit_ground = - 2 * initial_velocity_y / GRAVITY
    horizontal_distance = initial_velocity_x * time_to_hit_ground

    # ------------------------------------
    # Output the Results
    print("\nTime to hit the ground: {:.2f} seconds".format(time_to_hit_ground))
    print("\nThe horizontal distance the projectile traveled is: {:.2f} meters".format(horizontal_distance))
#endregion

#endregion

#region MAIN PROGRAM

# Welcome
print(WELCOME_MESSAGE)
gameMode = 1
quit = False
while not quit:

    # Menu
    print(MAIN_MENU)
    choice = getString("Enter your choice (1,2,3,q): ")

    if choice == 'q':
        quit = True
        continue
    elif choice == "1": gameMode = 1
    elif choice == "2": gameMode = 2
    elif choice == "3": gameMode = 3
    else: continue
    
    playGame()
    
exit()


        # ------------------------------------
    # Start Game
    playAgain = True
    while playAgain:
        
        # ------------------------------------
        # Initialize Game
        # get random starting distance to 1 decimal place
        targetDistance = float(random.randint(MIN_START_DISTANCE*10, MAX_START_DISTANCE*10)) / 10.0
        # reset the number of shots for next round
        num_shots = 0
        # reset winning condition back to false
        game_win = False

        shootAgain = True
        while shootAgain:
            try:
                # ------------------------------------
                # Get User Input
                print("\nTarget distance is {:.1f} meters.".format(targetDistance))
                initial_angle = float(input("Enter the initial angle of the canon in degrees (0-90): "))
            except ValueError:
                print("Invalid input. Please enter a decimal number.")
                continue

            # ------------------------------------
            # Data Validation
            # Check if the user input for initial angle is between 0 and 90
            if not 0 <= initial_angle <= 90:
                print("Invalid input. Please enter a positive number for the initial angle between 0 and 90 degrees.")
                continue
            
            # successful shot so increment number of shots
            num_shots += 1

            # Convert the initial angle from degrees to radians
            initial_angle = initial_angle * (PI / 180.0)
            #initial_angle = math.radians(initial_angle)

            # Calculate the initial velocity in the x and y directions
            initial_velocity_x = INITIAL_VELOCITY * math.cos(initial_angle)
            initial_velocity_y = INITIAL_VELOCITY * math.sin(initial_angle)

            # Time iterations
            time = 0
            position_x = 0
            position_y = 0

            # Manually output the initial time and position
            print("Initial time and position: {:.2f} seconds, x: {:.2f} meters, y: {:.2f} meters".format(time, position_x, position_y))

            while position_y >= 0:
                time = time + TIME_INTERVAL

                position_x = initial_velocity_x * time
                position_y = initial_velocity_y * time + 0.5 * GRAVITY * time ** 2

                # output starting height and time
                print("Time {:.2f} seconds, x = {:.2f}m, y = {:.2f}m.".format(time, position_x, position_y))

            # --- end time interval loop ---



            # ------------------------------------
            # check if hit or not
            if abs(horizontal_distance - targetDistance) < HIT_DISTANCE:
                print("You hit the target at {:.2f} meters!".format(targetDistance))
                shootAgain = False
                game_win = True
            # check if killed yourself
            elif horizontal_distance  < SELF_DESTRUCT_DISTANCE:
                print("You self-destructed, oh no!  Game Over!")
                shootAgain = False
            # check if shot was too short
            elif horizontal_distance < targetDistance:
                print("You missed short by %.2f meters." % (targetDistance-horizontal_distance))
                print("Try again.")
            # check if shot was too long
            else:
                print("You overshot by %.2f meters." % (horizontal_distance-targetDistance))
                print("Try again.")

            # Hard and Expert Mode
            if gameMode == 2 or gameMode == 3: 
                move_distance = float(random.randint(20*10, 50*10))/10.0
                print("Your tank moved {:.1f} meters towards the target.".format(move_distance))
                targetDistance -= move_distance

            # Expert Mode Only
            if gameMode == 3:
                move_distance = float(random.randint(-100*10, 100*10))/10.0
                print("The target moved {:.1f} meters.".format(move_distance))
                targetDistance += move_distance
                
        # end shoot again loop

        if game_win:
            print("Congratulations! You hit the target in %i shots!" % num_shots)
        # ------------------------------------
        # Ask the user if they want to do another calculation
        playAgain = input("\nDo you want to play again? (y or n): ").lower() == "y"

    # --- end play again while loop ---
    
# --- end main menu loop     

print("Goodbye!")
exit()