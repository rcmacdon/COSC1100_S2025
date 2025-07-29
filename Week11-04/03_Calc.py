# -------------------------------------------
# My Calculator Example
# Clint MacDonald
# July 25, 2025
# -------------------------------------------

#region IMPORTS
import tkinter as tk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
# for comboboxes
from tkinter import ttk

#endregion

#region Global Variable and Constants
    #region CONSTANTS and Global Vars
APPLICATION_TITLE = "My Calculator"
AUTHOR = "Clint MacDonald"
VERSION = "0.1"

ADD = "+"
SUBTRACT = "-"
DIVIDE = "÷"
MULTIPLY = "×"
    #end region

    #region UI Controls
window = tk.Tk()
lblTitle = tk.Label(window)
txtNum1 = tk.Entry(window)
txtNum2 = tk.Entry(window)
btnA = tk.Button(window) #Addition
btnS = tk.Button(window) #Subtraction
btnD = tk.Button(window) #Division
btnM = tk.Button(window) #Multiplication
lblOutput = tk.Label(window)
cboOperator = ttk.Combobox(window)
    #endregion

#endregion

#region FUNCTIONS
    #region EVENT HANDLERS
def btnA_click():
    showResult(str(do_calculation(ADD)))

def btnS_click():
    showResult(str(do_calculation(SUBTRACT)))

def btnM_click():
    showResult(str(do_calculation(MULTIPLY)))

def btnD_click():
    result = str(do_calculation(DIVIDE))
    showResult(result)

def cboOperator_click():
    result = str(do_calculation(cboOperator.get()))

    #endregion

    #region Custom Functions
def initializeUI():
    #window
    window.title(APPLICATION_TITLE + " (" + VERSION + ")")
    window.geometry("400x400")

    # row 0
    lblTitle.config(text=APPLICATION_TITLE, border=2, font=("Arial Bold", 20))
    lblTitle.grid(row=0, column=0, columnspan=4, sticky="WE")

    # row 1
    txtNum1.config(width=10)
    txtNum1.grid(row=1, column=1, sticky="W")
    txtNum2.config(width=10)
    txtNum2.grid(row=1, column=2, sticky="E")

    #row 2
    btnA.config(text=ADD, command=btnA_click)
    btnA.grid(row=2, column=0, sticky="WE")
    btnS.config(text=SUBTRACT, command=btnS_click)
    btnS.grid(row=2, column=1, sticky="WE")
    btnM.config(text=MULTIPLY, command=btnM_click)
    btnM.grid(row=2, column=2, sticky="WE")
    btnD.config(text=DIVIDE, command=btnD_click)
    btnD.grid(row=2, column=3, sticky="WE")

    #row 3
    cboOperator.config(width=15)
    cboOperator.bind("<<ComboboxSelected>>", cboOperator_click)

    cboOperator['values'] = (ADD, SUBTRACT, MULTIPLY, DIVIDE)
    cboOperator.grid(row=3, column=0, columnspan=4)

    #row 4
    lblOutput.config(bg="lightgrey", text="")
    lblOutput.grid(row=4, column=0, columnspan=4, sticky="WE")

    # AODA
    Hovertip(txtNum1, "Enter the first number")
    Hovertip(txtNum2, "Enter the second number")
    Hovertip(btnA, "Click to add the numbers")
    Hovertip(btnS, "Click to subtract the numbers")
    Hovertip(btnM, "Click to multiply the numbers")
    Hovertip(btnD, "Click to divide the numbers")
    Hovertip(cboOperator, "Choose your mathematical operator!")

    #window.bind("<Escape>", lambda event: escape_key())
    #window.bind("<Return>", lambda event: enter_key())

def areNumbersValid():
    try:
        num1= float(txtNum1.get())
        num2= float(txtNum2.get())
        return True
    except ValueError as v:
        messagebox.showerror("Error", "Both entered values must be numeric!")
        return False

def do_calculation(operator: str):
    result = ""
    if areNumbersValid():
        num1 = float(txtNum1.get()) 
        num2 = float(txtNum2.get())
        if operator==ADD:
            result= num1 + num2
        elif operator == SUBTRACT:
            result = num1-num2
        elif operator == MULTIPLY:
            result = num1 * num2
        elif operator == DIVIDE:
            if not num2 == 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero!")
                result = "Error"

    return result

def showResult(result: str):
    lblOutput.config(text=result)

    #endregion
#endregion

#region Main Program
initializeUI()
window.mainloop()
#endregion

