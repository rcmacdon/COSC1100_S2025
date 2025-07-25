# ----------------------------
# Week 11 - tKinter
# Clint MacDonald
# July 24, 2025
# Our first tKinter Application
# ----------------------------

#region IMPORTS
import tkinter as tk
from tkinter import messagebox
from idlelib.tooltip import Hovertip
#endregion

#region Global Variables and constants
window = tk.Tk()
lblHello = tk.Label(window, text="Hello World", font=("Arial Bold", 20))
#endregion 

#region Functions

def initializeUI():
    window.title("Hello World Title")
    window.geometry("400x400")
    lblHello.pack()

#endregion

#region Main Program
initializeUI()
window.mainloop()
#endregion