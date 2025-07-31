#---------------------------------
# playing with Listboxes
# Clint MacDonald
# July 31, 2025
# --------------------------------

# LAST DEMO OF THE TERM
# --------------------------------

#region IMPORTS
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from idlelib.tooltip import Hovertip
#endregion

#region Constants and UI Controls
window = tk.Tk()
lbxAvailable = tk.Listbox(window, selectmode=tk.MULTIPLE, height=15, width=20)
lbxChosen = tk.Listbox(window, selectmode=tk.MULTIPLE, height=15, width=20)
#endregion

#region FUNCTIONS
    #region tools
def move_selected_items(source_listbox, destination_listbox):
    '''Move selected items from the source listbox to the destination listbox'''
    selected_items = source_listbox.curselection()
    for index in selected_items[::-1]: # Reverse to avoid index shifting
        item = source_listbox.get(index)  #Getting the value having the index number
        destination_listbox.insert(tk.END, item)  # inserting into the destination listbox
        source_listbox.delete(index)   # deleting from the source listbox
    sort_listbox(destination_listbox)

def move_all_items(source_listbox, destination_listbox):
    '''Move selected items from the source listbox to the destination listbox'''
    items = source_listbox.get(0, tk.END)
    for item in items:
        destination_listbox.insert(tk.END, item)  # inserting into the destination listbox
    source_listbox.delete(0, tk.END)   # deleting from the source listbox
    sort_listbox(destination_listbox)

def sort_listbox(target_listbox):
    '''sorts the values inside the target listbox'''
    items = target_listbox.get(0, tk.END) # copying items in box
    items = sorted(items)                          # sorting the new list
    target_listbox.delete(0, tk.END)      # deleting items from listbox
    for item in items:                    # adding newly sorted items back into the listbox
        target_listbox.insert(tk.END, item)

    #endregion

    #region events
def btnSelectAll_Click():
    move_all_items(lbxAvailable, lbxChosen)
def btnSelect_Click():
    move_selected_items(lbxAvailable, lbxChosen)
def btnDeselect_Click():
    move_selected_items(lbxChosen, lbxAvailable)
def btnDeselectAll_Click():
    move_all_items(lbxChosen, lbxAvailable)

def btnExit_Click():
    if messagebox.askyesno("Exit Confirmation", "Do you want to quit?"):
        exit()
    #endregion

    #region ui
def create_ui():
    '''Creates the controls and places them on the ui'''
    #window
    window.title("Listbox Fun")
    window.geometry("345x310")
    window.resizable(False, False)
    #row0
    lbxAvailable.grid(row=0, column=0, rowspan=4, padx=10, pady=10)
    btnSelectAll = tk.Button(window, text=">>", width=5, command=btnSelectAll_Click)
    btnSelectAll.grid(row=0, column=1, padx=5, pady=5)
    lbxChosen.grid(row=0, column=2, rowspan=4, padx=5, pady=5)
    #row1
    btnSelect = tk.Button(window, text=">", width=5, command=btnSelect_Click)
    btnSelect.grid(row=1, column=1, padx=5, pady=5)
    #row2
    btnDeselect = tk.Button(window, text="<", width=5, command=btnDeselect_Click)
    btnDeselect.grid(row=2, column=1, padx=5, pady=5) 
    #row3
    btnDeselectAll = tk.Button(window, text="<<", width=5, command=btnDeselectAll_Click)
    btnDeselectAll.grid(row=3, column=1, padx=5, pady=5)
    #row4
    btnExit = tk.Button(window, text="Exit", width=7, command=btnExit_Click)
    btnExit.grid(row=4, column=2, padx=5, pady=5, sticky="E")

def load_data():
    '''Load data into the various controls on the form during loading'''
    available_items = ["Red", "Yellow", "Blue", "Green", "Violet", "Orange", "Purple", "White", "Black"]
    available_items.sort()
    for item in available_items:
        lbxAvailable.insert(tk.END, item)


    #endregion
#endregion

#region Main Code
create_ui()
load_data()
window.mainloop()
exit()
#endregion