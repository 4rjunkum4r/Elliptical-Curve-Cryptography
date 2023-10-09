import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Key Generator")
root.resizable(width=False, height=False)

mainframe = tk.Frame(root)
mainframe.grid(row=0, column=0, padx=10, pady=10)

intro = """
Welcome to pair key generations, Here you can generate the keys for two different user. Use the checkbox to select on which curve you want to generate keys
"""

intro_lb = tk.Label(mainframe,
                    text=intro, wraplength=500,
                    font=("Cambria", 15, "bold"))
intro_lb.grid(row=0, columnspan=1, padx=1, pady=1)

man_img = Image.open('Images\Icons\man.png')
man_img_resized = man_img.resize((60, 60))

man_icon = ImageTk.PhotoImage(man_img_resized)
man_icon_label = tk.Label(
    mainframe, image=man_icon, border=5, width=50, height=50
)
man_icon_label.grid(row=1, column=0, pady=15)

user_a_lb = tk.Label(
    mainframe, text='User Key Generation', border=1, relief='groove')
user_a_lb.grid(row=2, column=0, pady=15)

# woman_img = Image.open('Images\Icons\woman.png')
# woman_img_resized = woman_img.resize((60, 60))
# 6
# woman_icon = ImageTk.PhotoImage(woman_img_resized)
# woman_icon_label = tk.Label(
#     mainframe, image=woman_icon, border=5, width=50, height=50
# )
# woman_icon_label.grid(row=1, column=1)

# user_b_lb = tk.Label(
#     mainframe, text='User B Key Generation', border=1, relief='groove')
# user_b_lb.grid(row=2, column=1)


#
#
#
#
#
#
#


curve_label = tk.Label(mainframe, bg='white', width=20,
                       text='Select the curve please')
curve_label.grid(row=4, column=0)


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
combobox.grid(row=3, column=0)


# curve_combobox=tk.StringVar()

# curve_combobox_list=ttk.Combobox(mainframe,textvariable=curve_combobox,values=[("Select the curve"),("brainpoolP256r1"),("secp256k1")])
# curve_combobox_list.current(1)
# curve_combobox_list.config(height=1,state='readonly')
# curve_combobox_list.grid(row=3,column=0, pady=15)

# selected_option=curve_combobox.get()

# image_label = tk.Label(root, text=selected_option)
# image_label.grid(row=5, column=0)


#
#
#
#
#
def generateKey():
    gen_btn.config(text="Re-Generate")


gen_btn = tk.Button(
    mainframe,
    text="GENERATE",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"), command=generateKey)
gen_btn.grid(row=5, column=0)

key_text_area = tk.Text(mainframe, state="disabled", width=50, height=5)
key_text_area.grid(row=6, column=0)

save_button = tk.Button(
    mainframe,
    text="Save",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"))
save_button.grid(row=7, column=0)

root.mainloop()
