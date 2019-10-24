import tkinter as tk
from tkinter import messagebox

class App(tk.Frame):

    def __init__(self, master):
        self.master = master

        lbl1 = tk.Label(self.master, text = "Enter 2 numbers to be added \ntogether and click submit")
        lbl1.grid(row = 0, column = 0, columnspan = 3)
if __name__ == "__main__":

    root = tk.Tk()
    myapp = App(root)
    root.mainloop()
