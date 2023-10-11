import tkinter as tk
import os
from tkinter import filedialog as fd


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
intro_lb.grid(row=0, columnspan=2, padx=1, pady=1)

#####################################
######################################


def txt2ascii(st):     # converts text to ascii
    ascii_string = []
    for i in st:
        ascii_string.append(ord(i))
    return ascii_string


def get_text_from_text_area_for_encryption():
    global user_input
    encrypt_text_area.config(state="normal")
    encrypt_text_area.delete("1.0", "end-1c")
    user_input = to_be_encrypt_text_area.get("1.0", "end-1c")
    uni_coded_text = txt2ascii(user_input)
    encrypt_text_area.insert("end-1c", uni_coded_text)


def get_text_from_text_area_for_decryption():
    global user_input_de
    decrypt_text_area.config(state="normal")
    decrypt_text_area.delete("1.0", "end-1c")
    user_input_de = to_be_decrypt_text_area.get("1.0", "end-1c")
    decrypt_text_area.insert("end-1c", user_input_de)


to_be_encrypt_label = tk.Label(
    mainframe, text="Encryption Part", relief="groove")
to_be_encrypt_label.grid(row=1, column=0, pady=15)

to_be_decrypt_label = tk.Label(
    mainframe, text="Decryption Part", relief="groove")
to_be_decrypt_label.grid(row=1, column=1, pady=15)

to_be_encrypt_text_area = tk.Text(
    mainframe, width=50, height=5, state="normal")
to_be_encrypt_text_area.grid(row=2, column=0, pady=15, padx=15)

public_key_button = tk.Button(
    mainframe, text="Upload public key of recipient", border=5
)
public_key_button.grid(row=3, column=0)

private_key_button = tk.Button(
    mainframe, text="Upload private key of recipient", border=5
)
private_key_button.grid(row=3, column=1)

save_button = tk.Button(
    mainframe,
    text="Encrypt",
    border=5, command=get_text_from_text_area_for_encryption)
save_button.grid(row=4, column=0, pady=15)

to_be_decrypt_text_area = tk.Text(
    mainframe, width=50, height=5, state="normal")
to_be_decrypt_text_area.grid(row=2, column=1, pady=15, padx=15)


save_button = tk.Button(
    mainframe,
    text="Decrypt",
    border=5, command=get_text_from_text_area_for_decryption)
save_button.grid(row=4, column=1, pady=15)

###########################################
##########################################

encrypt_label = tk.Label(mainframe, text="Your Encrypted Message")
encrypt_label.grid(row=5, column=0, pady=15)

decrypt_label = tk.Label(mainframe, text="Your Decrypted Message")
decrypt_label.grid(row=5, column=1, pady=15)

encrypt_text_area = tk.Text(mainframe, width=50, height=5)
encrypt_text_area.grid(row=6, column=0, pady=15, padx=15)

decrypt_text_area = tk.Text(mainframe, width=50, height=5)
decrypt_text_area.grid(row=6, column=1, pady=15, padx=15)


def save_encrypting_mesage():
    global user_input
    if user_input is not None:
        file_path = fd.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(str(user_input) + "\n")


def save_decrypting_mesage():
    global user_input_de
    if user_input_de is not None:
        file_path = fd.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(str(user_input_de) + "\n")


save_button = tk.Button(
    mainframe,
    text="Save",
    border=5, command=save_encrypting_mesage)
save_button.grid(row=7, column=0, pady=15)

save_button = tk.Button(
    mainframe,
    text="Save",
    border=5, command=save_decrypting_mesage)
save_button.grid(row=7, column=1, pady=15)


###########################################
#########################################


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
    border=5, command=lambda: open_window('WelcomePage.py'))
back_button.grid(row=8, columnspan=2, pady=15)

root.mainloop()
