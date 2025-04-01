import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from datetime import datetime, timedelta

# Initialize Tkinter
root = tk.Tk()
root.title("24-hour Timetable Management")

# Set the start date
start_date = datetime(2025, 3, 31)

# Create a frame for the calendar
calendar_frame = ttk.Frame(root)
calendar_frame.pack()

# Create a label to display the current date
date_label = ttk.Label(calendar_frame)
date_label.pack()

# Create a frame for the timetable
timetable_frame = ttk.Frame(root)
timetable_frame.pack()

# Load timetable from Excel
timetable = pd.read_excel("timetable.xlsx")

# Create a treeview to display the timetable
treeview = ttk.Treeview(timetable_frame, columns=list(timetable.columns), show="headings")
for column in timetable.columns:
    treeview.heading(column, text=column)
treeview.pack()

# Function to update the date and timetable
def update():
    global start_date
    date_label.config(text=start_date.strftime("%Y-%m-%d"))
    for index, row in timetable.iterrows():
        treeview.insert("", "end", values=list(row))
    start_date += timedelta(days=1)

# Button to go to the next day
next_button = ttk.Button(root, text="Next", command=update)
next_button.pack()

# Start the Tkinter main loop
root.mainloop()
