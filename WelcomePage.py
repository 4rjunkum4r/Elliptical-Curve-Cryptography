import tkinter as tk

root = tk.Tk()
root.title("WELCOME")
root.geometry("500x500")  # Size of my window
# root.resizable(width=False, height=False)
root.rowconfigure(0)
root.columnconfigure(0)

mainframe = tk.Frame(root)
mainframe.grid(row=0, column=0)

introduction="Hi, welcome to my small tool which will provide you method to encrypt or decrypt your data based on Elliptical Curve Cryptography. I hope you will like it. ☺️Keep smiling ☺️"

intro_lb=tk.Label(mainframe,
                      text=introduction,
                      border=10)
intro_lb.grid(row=1,column=0)

gen_btn = tk.Button(
    mainframe,
    text="CLICK HERE TO GENERATE THE KEY PAIR",
    cursor="pirate",
    width=50,
    background='Black',
    foreground='White',    
    border=10)
gen_btn.grid(row=2, column=0)

seperator=tk.Label(mainframe,
                   text="")
seperator.grid(row=3,column=0)

gen_btn = tk.Button(
    mainframe,
    text="CLICK HERE TO SECURE YOUR FILE",
    cursor="pirate",
    width=50,
    background='Black',
    foreground='White',    
    border=10)
gen_btn.grid(row=4, column=0)

root.mainloop()
