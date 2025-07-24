# ------------------------------
# COSC1100 - Week 11 Class 2 Demo
# Clint MacDonald
# July 24, 2025
# Calculator Applications
# ------------------------------

#region IMPORTS
import tkinter as tk
from idlelib.tooltip import Hovertip
from tkinter import messagebox

#endregion

#region GLOBAL VARIABLES

    #region VARIABLES
APPLICATION_TITLE = "My Calculator"
    #endregion

    #region CONTROLS
window = tk.Tk()
lblTitle = tk.Label(window, text=APPLICATION_TITLE, font=("Arial Bold", 20), bg="lightgrey", border=2, relief="solid")
txtNum1 = tk.Entry(window, width=6)
txtNum2 = tk.Entry(window, width=6)
btnAdd = tk.Button(window, text="+")
btnSubtract = tk.Button(window, text="-")
btnMultiply = tk.Button(window, text="*")
btnDivide = tk.Button(window, text="/")
lblOutput = tk.Label(window, text="", bg="lightgrey")
    #endregion
#endregion

#region FUNCTIONS

#region EVENT HANDLERS
def click_btnAdd():
    if areNumbersValid():
        result = doCalculations(float(txtNum1.get()), float(txtNum2.get()), "+")
        lblOutput.config(text=str(result))

def click_btnSubtract():
    if areNumbersValid():
        lblOutput.config(text=str(doCalculations(float(txtNum1.get()), float(txtNum2.get()), "-")))

def click_btnMultiply():
    if areNumbersValid():
        result = doCalculations(float(txtNum1.get()), float(txtNum2.get()), "*")
        lblOutput.config(text=str(result))

def click_btnDivide():
    if areNumbersValid():
        result = doCalculations(float(txtNum1.get()), float(txtNum2.get()), "/")
        lblOutput.config(text=str(result))

def escape_key():
    pass

def enter_key():
    pass

    #endregion


    #region CUSTOM FUNCTIONS

def initializeLayout():
    #window
    window.title(APPLICATION_TITLE + " by Clint")
    window.geometry("200x200")
    #row 0
    lblTitle.grid(row=0, column=0, columnspan=4, sticky="WE")
    #row 1
    txtNum1.grid(row=1, column=0, sticky="E")
    txtNum2.grid(row=1, column=2, sticky="W")
    #row 2

    btnAdd.config(command=click_btnAdd)
    btnAdd.grid(row=2, column=0, sticky="WE")

    btnSubtract.config(command=click_btnSubtract)
    btnSubtract.grid(row=2, column=1, sticky="WE")
    
    btnMultiply.config(command=click_btnMultiply)
    btnMultiply.grid(row=2, column=2, sticky="WE")
    
    btnDivide.config(command=click_btnDivide)
    btnDivide.grid(row=2, column=3, sticky="WE")
    #row 3
    lblOutput.grid(row=3, column=0, columnspan=4, sticky="WE")

    # Tool Tips
    Hovertip(txtNum1, "Enter the first number!")
    Hovertip(txtNum2, "Enter the second number!")
    Hovertip(btnAdd, "Click to add the numbers together!")
    Hovertip(btnSubtract, "Click to subtract the numbers!")
    Hovertip(btnMultiply, "Click to multiply the numbers together!")
    Hovertip(btnDivide, "Click to divide the numbers!")
    
    # Key Binds
    window.bind("<Escape>", lambda event: escape_key())
    window.bind("<Return>", lambda event: enter_key())

def areNumbersValid():
    try:
        num1 = float(txtNum1.get())
        num2 = float(txtNum2.get())

        return True
    except ValueError as v:
        messagebox.showerror("Error","You must enter numeric values!")
        return False
    
def doCalculations(num1:float, num2:float, operator:str):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if not num2 == 0:
            result = num1 / num2
        else: 
            messagebox.showerror("Error", "Division by zero")
            result = ""
    
    return result

    #endregion

#endregion

#region MAIN PROGRAM
initializeLayout()
window.mainloop()
#endregion

