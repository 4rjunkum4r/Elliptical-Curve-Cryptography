from tkinter import *
from tkinter import ttk

root = Tk()
root.title("WELCOME")
root.geometry("500x500")  # Size of my window
root.resizable(width=False,height=False)

mainframe = ttk.Frame(root)
mainframe.grid(row=0, column=0)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

ttk.Button(mainframe, text="Click to generate pair of keys", width=50).grid(
    row=0, column=0, sticky=W)
ttk.Button(mainframe, text="Click to secure your file", width=50).grid(
    row=1, column=0, sticky=W)

root.mainloop()
