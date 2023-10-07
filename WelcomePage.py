import tkinter as tk
import os
import sys

root = tk.Tk()
root.title("WELCOME")  # Size of my window
root.resizable(width=False, height=False)

mainframe = tk.Frame(root)
mainframe.grid(row=0, column=0, padx=20, pady=20)

introduction = """
Hi, welcome to my small tool which will provide you method to encrypt or decrypt your data based on Elliptical Curve Cryptography. I hope you will like it. Keep smiling
"""

intro_lb = tk.Label(mainframe,
                    text=introduction,
                    wrap=500, font=("Cambria", 15, "bold"))
intro_lb.grid(row=0, column=0, padx=1, pady=1)


def open(filename):
    os.chdir(
        "C:\\Users\\kumar\\Desktop\\CAP791 Project\\Elliptical-Curve-Cryptography")
    # runnning the python command on cmd to execute both windows
    os.system('python '+filename)


gen_btn = tk.Button(
    mainframe,
    text="CLICK HERE TO GENERATE THE KEY PAIR",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"), command=lambda: open("Key.py"))
gen_btn.grid(row=1, column=0)

seperator = tk.Label(mainframe,
                     text="")
seperator.grid(row=2, column=0)

gen_btn = tk.Button(
    mainframe,
    text="CLICK HERE TO SECURE YOUR FILE",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"), command=lambda: open("Tool.py"))
gen_btn.grid(row=3, column=0)

root.mainloop()
