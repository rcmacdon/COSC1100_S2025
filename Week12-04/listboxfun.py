#---------------------------------
# playing with Listboxes
# Clint MacDonald
# August 1, 2025
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


#region Functions
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

def btnSelectAll_Click():
    '''Selects all items in the available listbox and moves them to the chosen listbox'''
    if lbxAvailable.size() == 0:
        messagebox.showinfo("No Items", "There are no items to select.")
        return
    move_all_items(lbxAvailable, lbxChosen)

def btnSelect_Click():
    '''Selects the highlighted items in the available listbox and moves them to the chosen listbox'''
    move_selected_items(lbxAvailable, lbxChosen)

def btnDeselect_Click():
    '''Deselects the highlighted items in the chosen listbox and moves them back to the available listbox'''
    move_selected_items(lbxChosen, lbxAvailable)

def btnDeselectAll_Click():
    '''Deselects all items in the chosen listbox and moves them back to the available listbox'''
    if lbxChosen.size() == 0:
        messagebox.showinfo("No Items", "There are no items to deselect.")
        return
    move_all_items(lbxChosen, lbxAvailable)

def btnExit_Click():
    '''Exits the application'''
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        exit()

def move_selected_items(source_listbox, destination_listbox):
    '''Moves selected items from source_listbox to target_listbox'''
    selected_indices = source_listbox.curselection()
    if not selected_indices:
        messagebox.showinfo("No Selection", "Please select an item to move.")
        return
    for index in selected_indices[::-1]:  # Reverse to avoid index shifting
        item = source_listbox.get(index)
        destination_listbox.insert(tk.END, item)
        source_listbox.delete(index)
    sort_listbox(destination_listbox)

# function to move all items from one listbox to another
def move_all_items(source_listbox, destination_listbox):
    '''Moves all items from source_listbox to destination_listbox'''
    items = source_listbox.get(0, tk.END)
    for item in items:
        destination_listbox.insert(tk.END, item)
    source_listbox.delete(0, tk.END)
    sort_listbox(destination_listbox)


def sort_listbox(listbox):
    '''Sorts the items in the given listbox'''
    items = listbox.get(0, tk.END)
    items = sorted(items)
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)


def load_data():
    '''Loads data into the available listbox'''
    items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew"]
    items.sort()
    for item in items:
        lbxAvailable.insert(tk.END, item)


def main():
    '''Main function to run the application'''
    create_ui()
    load_data()
    window.mainloop()

main()
exit()