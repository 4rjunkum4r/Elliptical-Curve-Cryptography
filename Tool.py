import tkinter as tk
import os
root = tk.Tk()
root.title("Tool")
root.resizable(width=False, height=False)

mainframe = tk.Frame(root)
mainframe.grid(row=0, column=0, padx=20, pady=20)

introduction = """
Now it's easy to encrypt and decrypt your file, just do before every exchange of secret stuffs
"""

intro_lb = tk.Label(mainframe,
                    text=introduction,
                    wrap=500, font=("Cambria", 15, "bold"))
intro_lb.grid(row=0, column=0, padx=1, pady=1)


def open(filename):
    root.destroy()
    mainframe.mainloop()
    os.chdir(
        "C:\\Users\\kumar\\Desktop\\CAP791 Project\\Elliptical-Curve-Cryptography")
    # runnning the python command on cmd to execute both windows
    os.system('python '+filename)


back_button = tk.Button(
    mainframe,
    text="BACK",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"), command=lambda: open('WelcomePage.py'))
back_button.grid(row=8, columnspan=2, pady=15)

root.mainloop()
