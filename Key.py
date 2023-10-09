# IMPORT PACKAGES / MODULE / LIBRARIES
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Creating Frame here for gui mode
root = tk.Tk()
root.title("Key Generator")
root.resizable(width=False, height=False)
mainframe = tk.Frame(root)
mainframe.grid(row=0, column=0, padx=10, pady=10)

# Heading for the current page
intro = """
Welcome to pair key generations, Here you can generate the keys for two different user. Use the checkbox to select on which curve you want to generate keys
"""

# Creating and placing Label Widget into the frame
intro_lb = tk.Label(mainframe, wraplength=750,
                    text=intro,
                    font=("Cambria", 15, "bold"))
intro_lb.grid(row=0, columnspan=2)

# Creating icon on Image used from PIL module
man_img = Image.open('Images\Icons\man.png')

# Resizing as per requirement
man_img_resized = man_img.resize((60, 60))

# Using PhotoImage widgets of PIL
man_icon = ImageTk.PhotoImage(man_img_resized)
man_icon_label = tk.Label(
    mainframe, image=man_icon, border=5, width=50, height=50
)
man_icon_label.grid(row=1, column=0, pady=15)

user_man_lb = tk.Label(
    mainframe, text='User Key Generation', border=1, relief='groove')
user_man_lb.grid(row=2, column=0, pady=15)

# same for woman user
woman_img = Image.open('Images\Icons\woman.png')
woman_img_resized = woman_img.resize((60, 60))
6
woman_icon = ImageTk.PhotoImage(woman_img_resized)
woman_icon_label = tk.Label(
    mainframe, image=woman_icon, border=5, width=50, height=50
)
woman_icon_label.grid(row=1, column=1)

user_woman_lb = tk.Label(
    mainframe, text='User B Key Generation', border=1, relief='groove')
user_woman_lb.grid(row=2, column=1)

# Providing user to choose curve based on which a keys can be generate
curve_label = tk.Label(mainframe, bg='white', width=20,
                       text='Select the curve please')
curve_label.grid(row=4, columnspan=2, pady=15)


def print_selection(event):
    option_selected = var.get()
    if option_selected == "brainpoolP256r1":
        curve_label.config(text='Selected brainpoolP256r1')
    elif option_selected == "secp256k1":
        curve_label.config(text='Selected secp256k1')
    else:
        curve_label.config(text='Select the curve')


var = tk.StringVar()
combobox = ttk.Combobox(mainframe, textvariable=var, values=[
                        "Click to see list of curves ", "brainpoolP256r1", "secp256k1"], state='readonly', width=25)
combobox.current(0)

# Bind the `print_selection()` function to the `<<ComboboxSelected>>` event.
combobox.bind("<<ComboboxSelected>>", print_selection)
combobox.grid(row=3, columnspan=2, pady=15)


def generate_man_key():
    generate_man_button.config(text="Re-Generate")


generate_man_button = tk.Button(
    mainframe,
    text="GENERATE",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"), command=generate_man_key)
generate_man_button.grid(row=5, column=0, pady=15)

key_text_area = tk.Text(mainframe, state="disabled", width=50, height=5)
key_text_area.grid(row=6, column=0, pady=15)

save_button = tk.Button(
    mainframe,
    text="Save",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"))
save_button.grid(row=7, column=0, pady=15)

def generate_woman_key():
    generate_woman_button.config(text="Re-Generate")

generate_woman_button = tk.Button(
    mainframe,
    text="GENERATE",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"), command=generate_woman_key)
generate_woman_button.grid(row=5, column=1, pady=15)

key_text_area = tk.Text(mainframe, state="disabled", width=50, height=5)
key_text_area.grid(row=6, column=1, pady=15, padx=15)

save_button = tk.Button(
    mainframe,
    text="Save",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"))
save_button.grid(row=7, column=1, pady=15)

root.mainloop()
