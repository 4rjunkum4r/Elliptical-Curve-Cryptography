# IMPORT PACKAGES / MODULE / LIBRARIES
import os
import secrets
import tkinter as tk
from tkinter import ttk
from tinyec import registry
from PIL import Image, ImageTk
from tkinter import filedialog

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
    mainframe, text='User A Key Generation', border=1, relief='groove')
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
    option_selected = curve_option.get()
    if option_selected == "brainpoolP256r1":
        curve_label.config(text='Selected brainpoolP256r1')
    elif option_selected == "secp256r1":
        curve_label.config(text='Selected secp256r1')
    elif option_selected == "brainpoolP512r1":
        curve_label.config(text='Selected brainpoolP512r1')
    else:
        curve_label.config(text='Select the curve')


curve_option = tk.StringVar()
combobox = ttk.Combobox(mainframe, textvariable=curve_option, values=[
                        "Click to see list of curves ", "brainpoolP256r1", "secp256r1", "brainpoolP512r1"], state='readonly', width=25)
combobox.current(0)

# Bind the `print_selection()` function to the `<<ComboboxSelected>>` event.
combobox.bind("<<ComboboxSelected>>", print_selection)
combobox.grid(row=3, columnspan=2, pady=15)


def generate_man_key():
    global man_private_key
    global man_public_key
    global man_public_key_int
    curve_name = curve_option.get()
    # The elliptic curve which is used for the ECDH calculations
    curve = registry.get_curve(curve_name)
    # Generation of secret key and public key

    man_private_key = secrets.randbelow(curve.field.n)

    man_public_key = man_private_key * curve.g
    man_public_key_int = hex(man_public_key.x) + hex(man_public_key.y % 2)[2:]

    user_man_key_text_area.config(state="normal")
    user_man_key_text_area.delete("1.0", tk.END)
    user_man_key_text_area.insert(tk.END, man_public_key_int)
    user_man_key_text_area.config(state="disabled")
    generate_man_button.config(text="Re-Generate")


generate_man_button = tk.Button(
    mainframe,
    text="GENERATE",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"), command=generate_man_key)
generate_man_button.grid(row=5, column=0, pady=15)

# man_private_key = generate_man_key()

user_man_key_text_area = tk.Text(
    mainframe, state="disabled", width=50, height=5)
user_man_key_text_area.grid(row=6, column=0, pady=15)


def save_man_keys():
    global man_private_key, man_public_key, man_public_key_int
    if man_private_key is not None and man_public_key is not None:
        file_path = tk.filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write("Man Private Key:\n")
                file.write(str(man_private_key) + "\n")
                file.write("Man Public Key:\n")
                file.write(str(man_public_key_int))


save_button = tk.Button(
    mainframe,
    text="Save",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"), command=save_man_keys)
save_button.grid(row=7, column=0, pady=15)


def generate_woman_key():
    global woman_private_key
    global woman_public_key
    global woman_public_key_int
    curve_name = curve_option.get()
    # The elliptic curve which is used for the ECDH calculations
    curve = registry.get_curve(curve_name)
    # Generation of secret key and public key

    woman_private_key = secrets.randbelow(curve.field.n)

    woman_public_key = woman_private_key * curve.g
    woman_public_key_int = hex(woman_public_key.x) + \
        hex(woman_public_key.y % 2)[2:]

    user_woman_key_text_area.config(state="normal")
    user_woman_key_text_area.delete("1.0", tk.END)
    user_woman_key_text_area.insert(tk.END, woman_public_key_int)
    user_woman_key_text_area.config(state="disabled")

    generate_woman_button.config(text="Re-Generate")


def compare_keys():
    A = man_private_key*woman_public_key
    A_s = hex(A.x) + \
        hex(A.y % 2)[2:]

    B = woman_private_key*man_public_key
    B_s = hex(B.x) + \
        hex(B.y % 2)[2:]
    if (A_s == B_s):
        compare_label = tk.Label(
            mainframe, bg='white', width=20, text='Keys matching')
        compare_label.grid(row=9, columnspan=2, pady=5)
    else:
        compare_label = tk.Label(
            mainframe, bg='white', width=20, text="Keys not matching")
        compare_label.grid(row=9, columnspan=2, pady=5)


compare_button = tk.Button(mainframe,
                           text="COMPARE",
                           cursor="pirate",
                           background='Black',
                           foreground='White',
                           border=5, font=("Cambria", 10, "bold"), command=compare_keys)
compare_button.grid(row=8, column=1, pady=5)

generate_woman_button = tk.Button(
    mainframe,
    text="GENERATE",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"), command=generate_woman_key)
generate_woman_button.grid(row=5, column=1, pady=15)

user_woman_key_text_area = tk.Text(
    mainframe, state="disabled", width=50, height=5)
user_woman_key_text_area.grid(row=6, column=1, pady=15, padx=15)


def save_woman_keys():
    global woman_private_key, woman_public_key
    if woman_private_key is not None and woman_public_key is not None:
        file_path = tk.filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write("Man Private Key:\n")
                file.write(str(woman_private_key) + "\n")
                file.write("Man Public Key:\n")
                file.write(str(woman_public_key_int))


save_button = tk.Button(
    mainframe,
    text="Save",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"), command=save_woman_keys)
save_button.grid(row=7, column=1, pady=15)


def open_window(filename):
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
    border=5, font=("Cambria", 10, "bold"), command=lambda: open_window('WelcomePage.py'))
back_button.grid(row=8, columnspan=2, pady=15)
root.mainloop()
