import tkinter as tk
import os
from tkinter import filedialog as fd
import random
from functions import operations, eccproperties

root = tk.Tk()
root.title("Tool")
root.resizable(width=False, height=False)

mainframe = tk.Frame(root)
mainframe.grid(row=0, column=0, padx=20, pady=20)

introduction = """
Now it's easy to encrypt and decrypt your message, just do before every exchange of secret stuffs
"""

intro_lb = tk.Label(mainframe,
                    text=introduction,
                    wrap=500, font=("Cambria", 15, "bold"))
intro_lb.grid(row=0, columnspan=2, padx=1, pady=1)

#####################################
######################################

a = 5829
b = 2079
p = 6277101735386680763835789423207666416083908700390324961279
private_key_A = 7487
private_key_B = 6737
G = [2436, 4951]
radom_integer = random.randint(
    0, 6277101735386680763835789423207666416083908700390324961279)

############################


def get_text_from_text_area_for_encryption():
    global user_input, cx1, cx2
    encrypt_text_area.config(state="normal")
    encrypt_text_area.delete("1.0", "end-1c")
    user_input = to_be_encrypt_text_area.get("1.0", "end-1c")
    asciiCoded = operations.txt2ascii(user_input)
    pairLength = len(operations.toDigits(p, 65536))-1
    groupList = operations.grouping(asciiCoded, pairLength)
    bigInt = operations.bigInteger(groupList)
    cipherPair = operations.grouping(bigInt, 2)
    cx1 = eccproperties.double_and_add(
        radom_integer, G, p, a)  # first half of ciphertxt
    pkey = eccproperties.double_and_add(private_key_B, G, p, a)
    lamxp = eccproperties.double_and_add(radom_integer, pkey, p, a)
    cx2 = []  # second half of cipher text
    for i in cipherPair:
        cx2.append(eccproperties.ecc_add(i[0], i[1], lamxp[0], lamxp[1], p, a))
    encrypt_text_area.insert("end-1c", str([cx1, cx2]))


def get_text_from_text_area_for_decryption():
    global user_input_de
    decrypt_text_area.config(state="normal")
    decrypt_text_area.delete("1.0", "end-1c")
    user_input_de = to_be_decrypt_text_area.get("1.0", "end-1c")
    l2 = eccproperties.double_and_add(private_key_B, cx1, p, a)
    Cipher = []  # pm
    for i in cx2:
        Cipher.append(eccproperties.ecc_add(i[0], i[1], l2[0], -l2[1], p, a))
    sml_Int = []
    for i in Cipher:
        for j in i:
            sml_Int.append(operations.toDigits(j, 65536))
    Dicipher = ""
    for i in sml_Int:
        for j in i:
            Dicipher = Dicipher + chr(j)

    decrypt_text_area.insert("end-1c", str(Dicipher))


to_be_encrypt_label = tk.Label(
    mainframe, text="Encryption Part", relief="groove")
to_be_encrypt_label.grid(row=1, column=0, pady=15)

to_be_decrypt_label = tk.Label(
    mainframe, text="Decryption Part", relief="groove")
to_be_decrypt_label.grid(row=1, column=1, pady=15)

to_be_encrypt_text_area = tk.Text(
    mainframe, width=50, height=5, state="normal")
to_be_encrypt_text_area.grid(row=2, column=0, pady=15, padx=15)


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
    global uni_coded_text
    if uni_coded_text is not None:
        file_path = fd.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(str(uni_coded_text) + "\n")


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
