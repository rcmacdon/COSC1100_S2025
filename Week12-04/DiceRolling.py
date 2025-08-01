# --------------------------------------
# Dice Rolling Simulator
# Clint MacDonald
# July 31, 2025
# --------------------------------------

#region IMPORTS
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from idlelib.tooltip import Hovertip
import random
#endregion

#region CONSTANTS AND CONTROLS
window = tk.Tk()
txtNumDice = tk.Entry(window, width=9)
cboNumSides = ttk.Combobox(window, width=9)
lbxResults = tk.Listbox(window, width=15, height=12)
#endregion

#region FUNCTIONS

    #region UI
def btnExit_click():
    '''Exits the application after a confirmation'''
    if messagebox.askyesno("Exit Confirmation", "Do you want to quit?"):
        exit()

def btnClear_click():
    '''Clears the items out of the listbox'''
    if messagebox.askyesno("Deletion Confirmation", "Are you sure you want to delete the dice roll history?"):
        lbxResults.delete(0, tk.END)

def btnRoll_click():
    '''Simulate the rolling sequences'''
    # validate the input
    if isRollValid(txtNumDice.get(), cboNumSides.get()):
        # roll the dice
        #diceRolls = []
        diceRolls = randomizeIntegers(int(txtNumDice.get()), 1, int(cboNumSides.get()))
        # display the output in the listbox
        displayRollsInLBox(diceRolls)

def displayRollsInLBox(rolls):
    output_string = ""
    for i in rolls:
        output_string += " " + str(i)
    lbxResults.insert(0, output_string)

def showOutput(title, messageText):
    messagebox.showerror(title, messageText)

# Initialize Controls
def initialize_controls():
    '''This function will create and place all the controls on the window'''
    window.title("Dice Rolling Tool")

    # Row 0
    lblTitle = tk.Label(window, text="Dice Rolling Tool", font=("Arial", 16), anchor="center")
    lblTitle.grid(row=0, column=0, columnspan=3)

    # Row 1
    lblNumDice = tk.Label(window, text="Number of Dice:")
    lblNumDice.grid(row=1, column=0, sticky="e")

    txtNumDice.grid(row=1, column=1, sticky="w")

    lbxResults.grid(row=1, column=2, rowspan=3, padx=10, sticky="nsew")

    # Row 2
    lblNumSides = tk.Label(window, text="Number of Sides:")
    lblNumSides.grid(row=2, column=0, sticky="e")   

    cboNumSides.grid(row=2, column=1, sticky="w")
    cboNumSides['values'] = (4, 6, 8, 10, 12, 20)

    # Row 3
    btnRoll = tk.Button(window, text="Roll", width=10, command=btnRoll_click)
    btnRoll.grid(row=3, column=1, padx=10, sticky="e")

    # Row 4
    btnClear = tk.Button(window, text="Clear", width=10, command=btnClear_click)
    btnClear.grid(row=4, column=1, padx=10, sticky="e")

    btnExit = tk.Button(window, text="Exit", width=10, command=btnExit_click)
    btnExit.grid(row=4, column=2, pady=10, padx=10, sticky="e")

    # Key Bindings
    window.bind("<Return>", lambda event: btnRoll_click())
    window.bind("<Escape>", lambda event: btnExit_click())
    window.bind("<Alt-c>", lambda event: btnClear_click())

    # Tooltips
    Hovertip(txtNumDice, "Enter the number of dice to roll.")
    Hovertip(cboNumSides, "Select the number of sides for the dice.")
    Hovertip(btnRoll, "Click to roll the dice.")
    Hovertip(btnClear, "Click to clear the results.")
    Hovertip(btnExit, "Click to exit the application.")
    Hovertip(lbxResults, "Results of the dice rolls.")
    #endregion

    #region Custom Functions

def main():
    initialize_controls()
    window.mainloop()

def isRollValid(input_string1: str, input_string2: str):
    return isStringNumeric(input_string1) and doesValueExist(input_string2)

def isStringNumeric(input: str):
    try:
        input = float(input)
        return True
    except ValueError:
        showOutput("Validation Error", "You have entered a value that is not numeric!")
        return False

def doesValueExist(input: str):
    if len(input) > 0: return True
    else:
        showOutput("Validation Error", "You left a value empty!")
        return False

def randomizeIntegers(num: int, min: int, max: int):
    listNums = []
    for i in range(0,num):
        listNums.append(random.randint(min, max))
    return listNums

    #endregion

#endregion

#region Main program
main()
exit()
#endregion