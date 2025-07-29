# ------------------------------
# Dice Rolling Application
# Clint MacDonald
# July 29, 2025
# Working with different controls and tools
# -----------------------------

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

def displayRollsInLbox(rolls):
    output_string = ""
    for i in rolls:
        output_string += " " + str(i)
    lbxResults.insert(0, output_string)

def btnRoll_click():
    pass
    # validate number of dice and validate the dice type
    if isRollValid(txtNumDice.get(), cboNumSides.get()):
        # randomize the data
        values = []
        for i in range(0, int(txtNumDice.get())):
            values.append(random.randint(1, int(cboNumSides.get())))
        # display the data in the listbox
        displayRollsInLbox(values)

def btnExit_click():
    if messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?"):
        exit()

def btnClear_click():
    lbxResults.delete(0, tk.END)

def showOutput(title: str, message: str):
    messagebox.showerror(title, message)
    
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

def isRollValid(text_value: str, text_value2: str):
    if isStringNumeric(text_value) and isValueExist(text_value2):  
        return True
    else: 
        return False

def isStringNumeric(input_string: str):
    try:
        value = float(input_string)
        return True
    except:
        showOutput("Validation Error", "You entered a value that is not numeric!")
        return False

def isValueExist(input_string: str):
    if len(input_string) > 0:
        return True
    else:
        showOutput("Validation Error", "You left a value empty!")
        return False

def main():
    initialize_controls()
    window.mainloop()
    #endregion
#endregion

#region Main Code
main()
exit()
#endregion