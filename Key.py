import tkinter as tk

root = tk.Tk()
root.title("Key Generator")
root.resizable(width=False, height=False)

mainframe = tk.Frame(root)
mainframe.grid(row=0, column=0, padx=20, pady=20)

introduction = """
Key generator page welcomes you to provide you to generate key
"""

intro_lb = tk.Label(mainframe,
                    text=introduction,
                    wrap=500, font=("Cambria", 15, "bold"))
intro_lb.grid(row=0, column=0, padx=1, pady=1)

root.mainloop()
