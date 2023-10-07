import tkinter as tk

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

root.mainloop()