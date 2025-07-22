# ---------------------------------------
# Title:    My Name Is Application
# Author:   Clint MacDonald
# Date:     July 22, 2025
# Purpose:  To create our first application using input controls
#           and demonstrating grid layout and events
# ---------------------------------------

#region IMPORTs
import tkinter as tk
from tkinter import messagebox  # import messagebox from tkinter
from idlelib.tooltip import Hovertip  # required for tooltips
#endregion

#region Define the main window
myWindow = tk.Tk()
myWindow.title("My Name is")
myWindow.geometry("400x200")
#endregion

#region define functions

#region Event Handlers
def btnGo_Click():
    userName = txtName.get()
    lblOutput.config(text="Hello %s" % userName)

def escape_key():
    result = messagebox.askyesno("Quit", "Do you want to quit?")
    if result == True:  # if the user clicked 'OK'
        myWindow.quit()
#endregion

#region Custom Functions  
#endregion
def initializeControls():
    #lblTitle
    lblTitle.grid(row=0, column=0, columnspan=2)
    lblName.grid(row=1, column=0)
    txtName.grid(row=1, column=1)
    btnGo.grid(row=2, column=1, sticky="e")
    lblOutput.grid(row=3, column=0, columnspan=2, sticky="ew")

    #tool tips
    Hovertip(txtName, "Enter your name here!")
    Hovertip(btnGo, "Click to see your name")

    #Keyboard Shortcuts
    myWindow.bind("<Return>", lambda event: btnGo_Click())
    myWindow.bind("<Escape>", lambda event: escape_key())
#endregion

#region Define Controls
lblTitle = tk.Label(myWindow, text="Welcome to 'My Name Is'", font=("Arial", 16))
txtName = tk.Entry(myWindow, width=10)
lblName = tk.Label(myWindow, text="Enter your name: ")
btnGo = tk.Button(myWindow, text="Go", command=btnGo_Click)
lblOutput = tk.Label(myWindow, text="", bg="lightgrey")
#endregion

#region Main Program
initializeControls()
myWindow.mainloop()

#endregion