# ----------------------------
# Week 11 - tKinter
# Clint MacDonald
# July 24, 2025
# My Name Is tKinter Application
# ----------------------------

#region IMPORTS
import tkinter as tk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
#endregion

#region variables and constants
window = tk.Tk()
lblName = tk.Label(window, text="Enter Name:")
txtName = tk.Entry(window, width=20)
btnGo = tk.Button(window, text="Go!")
lblOutput = tk.Label(window, text="")
#endregion

#region Functions

    #region Event Handlers
def btnGo_Click():
    name = txtName.get()
    lblOutput.config(text="Hello %s" % name)

def exit_program():
    result = messagebox.askyesno("Quit Confirmation", "Are you sure you want to quit?")
    if result:
        window.quit()
        
    #endregion

    #region Custom Functions
def initializeUI():
    window.title("My Name Is!")
    window.geometry("200x200")

    lblName.grid(row=0, column=0)
    txtName.grid(row=0, column=1, sticky="E")
    btnGo.config(command=btnGo_Click)
    btnGo.grid(row=1, column=1, sticky="E")
    lblOutput.config(bg="lightgrey")
    lblOutput.grid(row=2, column=0, columnspan=2, sticky="WE")

    Hovertip(txtName, "Enter you name here!")
    Hovertip(btnGo, "Click here to say hello!")

    window.bind("<Return>", lambda event: btnGo_Click())
    window.bind("<Escape>", lambda event: exit_program())
    
    #endregion

#endregion

#region Main Program
initializeUI()
window.mainloop()
#endregion 