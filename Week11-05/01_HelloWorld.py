# -------------------------------------------
# Title:    Hello World Application
# Author:   Clint MacDonald
# Date:     July 22, 2025
# Purpose:  To create our first windows ui application
# -------------------------------------------

# Import the TKinter Library
import tkinter as tk

# Create the Main Window
myWindow = tk.Tk()

# fill in properties of the window
myWindow.title("Hello World Title")
myWindow.geometry("400x400")

# add a label to the window
lblHello = tk.Label(myWindow, text="Hello World", font=("Arial Bold", 20))
lblHello.pack()

# Start the program
myWindow.mainloop()

