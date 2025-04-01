import tkinter as tk
from tkinter import ttk
from datetime import datetime

class BookReviewApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Book Review App")
        self.geometry("400x400")

        self.label_date = ttk.Label(self, text="Date: ")
        self.label_date.place(x=50, y=50)

        self.label_time = ttk.Label(self, text="Time: ")
        self.label_time.place(x=50, y=80)

        self.label_title = ttk.Label(self, text="Title: ")
        self.label_title.place(x=50, y=110)
        self.entry_title = ttk.Entry(self)
        self.entry_title.place(x=150, y=110)

        self.label_author = ttk.Label(self, text="Author: ")
        self.label_author.place(x=50, y=140)
        self.entry_author = ttk.Entry(self)
        self.entry_author.place(x=150, y=140)

        self.label_review = ttk.Label(self, text="Review: ")
        self.label_review.place(x=50, y=170)
        self.entry_review = ttk.Entry(self)
        self.entry_review.place(x=150, y=170)

        self.update_date_time()

    def update_date_time(self):
        current_time = datetime.now()
        self.label_date.config(text="Date: " + current_time.strftime("%Y-%m-%d"))
        self.label_time.config(text="Time: " + current_time.strftime("%H:%M:%S"))
        self.after(1000, self.update_date_time)

if __name__ == "__main__":
    app = BookReviewApp()
    app.mainloop()
