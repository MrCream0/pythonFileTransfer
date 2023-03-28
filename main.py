import os
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

root = tk.Tk(className='CreamyMovements')


icon_img = tk.PhotoImage(file="Resources/Images/undefined - Imgur.gif")

# Set the new icon for the GUI window
root.iconphoto(True, icon_img)
root.configure(background="#434854")

# Create input field for source directory
src_label = tk.Label(root, text="Source directory:")
src_label.pack()
src_entry = tk.Entry(root, width=50)
src_entry.pack()

# Create output field for destination directory
dest_label = tk.Label(root, text="Destination directory:")
dest_label.pack()
dest_entry = tk.Entry(root, width=50)
dest_entry.pack()

button_style = {"background": "#0078D7", "foreground": "white", "font": ("Arial", 12)}

def choose_source_dir():
    # Open a file dialog to choose the source directory
    src_dir = filedialog.askdirectory()
    src_entry.delete(0, tk.END)
    src_entry.insert(0, src_dir)

def choose_dest_dir():
    # Open a file dialog to choose the destination directory
    dest_dir = filedialog.askdirectory()
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, dest_dir)

def move_files():
    # Get the source and destination directories
    src_dir = src_entry.get()
    dest_dir = dest_entry.get()

    # Move all files and subfolders from the source directory to the destination directory
    for item in os.listdir(src_dir):
        src_item = os.path.join(src_dir, item)
        dest_item = os.path.join(dest_dir, item)
        shutil.move(src_item, dest_item)

    # Show a message box when the transfer is complete
    tk.messagebox.showinfo("Transfer Complete", "All files have been moved!")

# Create button to choose source directory
src_button = tk.Button(root, text="Choose Source Directory", command=choose_source_dir, **button_style)
src_button.pack()

# Create button to choose destination directory
dest_button = tk.Button(root, text="Choose Destination Directory", command=choose_dest_dir, **button_style)
dest_button.pack()

# Create button to initiate transfer
transfer_button = tk.Button(root, text="Transfer", command=move_files, **button_style)
transfer_button.pack()

root.mainloop()
