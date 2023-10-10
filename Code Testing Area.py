# import tkinter as tk


# window = tk.Tk()
# window.title('My Window')
# window.geometry('100x100')

# l = tk.Label(window, bg='white', width=20, text='empty')
# l.pack()

# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 0):
#         l.config(text='I love Python ')
#     elif (var1.get() == 0) & (var2.get() == 1):
#         l.config(text='I love C++')
#     elif (var1.get() == 0) & (var2.get() == 0):
#         l.config(text='I do not anything')
#     else:
#         l.config(text='I love both')

# var1 = tk.IntVar()
# var2 = tk.IntVar()
# c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
# c1.pack()
# c2 = tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
# c2.pack()

# window.mainloop()

###############################################################################################################################
###############################################################################################################################

# import tkinter as tk
# from tkinter import ttk


# root = tk.Tk()

# # Create a Tkinter Combobox variable.
# var = tk.StringVar()

# # Create two Tkinter Combobox widgets.
# combobox_abc = ttk.Combobox(root, textvariable=var, values=["Abc", "Def"])
# combobox_abc.current(0)
# combobox_abc.config(height=1)
# combobox_abc.config(state='readonly')

# # Create an image object for the default option.
# # image_abc = tk.PhotoImage(file="abc.png")

# # Set the image for the default option.
# # combobox_abc.config(image=image_abc)

# # # Place the Combobox widgets in the Tkinter window.
# combobox_abc.grid(row=0, column=0)

# # # Start the Tkinter mainloop.
# root.mainloop()

# # # Get the value of the Tkinter Combobox variable.
# # option_selected = var.get()

# # # Display the corresponding image in a Tkinter Label widget.
# # image_label = tk.Label(root, image=tk.PhotoImage(file=option_selected + ".png"))
# # image_label.grid(row=1, column=0)

###############################################################################################################################
###############################################################################################################################

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.title("Combobox Example")
# root.geometry('300x300')
# combo = ttk.Combobox(
#     root, values=["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"])
# combo.pack()


# def option_selected(event):
#     selected_option = combo.get()
#     print("You selected:", selected_option)


# combo.bind("<<ComboboxSelected>>", option_selected)
# root.mainloop()

###############################################################################################################################
###############################################################################################################################

# import tkinter as tk
# from tkinter import ttk

# window = tk.Tk()
# window.title('My Window')
# window.geometry('100x100')

# frame = tk.Frame(window)
# frame.pack()

# l = tk.Label(frame, bg='white', width=20, text='Select')
# l.pack()

# def print_selection(event):
#     option_selected = var.get()
#     if option_selected == "Python":
#         l.config(text='I love Python')
#     elif option_selected == "C++":
#         l.config(text='I love C++')
#     else:
#         l.config(text='Select')

# var = tk.StringVar()
# combobox = ttk.Combobox(frame, textvariable=var, values=["Python", "C++"], state='readonly')
# combobox.current(0)

# # Bind the `print_selection()` function to the `<<ComboboxSelected>>` event.
# combobox.bind("<<ComboboxSelected>>", print_selection)
# combobox.pack()

# window.mainloop()

################################################################

# import tkinter as tk

# root = tk.Tk()

# # Create the new window
# new_window = tk.Toplevel(root)

# # Create a function to destroy the current window and open the new window
# def change_window():
#     root.destroy()
#     new_window.mainloop()

# # Bind the function to the button's click event
# button = tk.Button(root, text="Click to switch windows", command=change_window)
# button.pack()

# # Start the mainloop
# root.mainloop()

#########################################################################################################

# # Importing required libraries used 
# # to perform arithmetic operations 
# # on elliptic curves 
# from tinyec import registry 
# import secrets 

# # Function to calculate compress point 
# # of elliptic curves 
# def compress(publicKey):
#     return hex(publicKey.x) + hex(publicKey.y % 2)[2:] 

# # The elliptic curve which is used for the ECDH calculations 
# curve = registry.get_curve('brainpoolP256r1') 

# # Generation of secret key and public key 
# Ka = secrets.randbelow(curve.field.n) 
# X = Ka * curve.g 
# print("X:", compress(X)) 
# Kb = secrets.randbelow(curve.field.n) 
# Y = Kb * curve.g 
# print("Y:", compress(Y)) 
# print("Currently exchange the publickey (e.g. through Internet)") 

# # (A_SharedKey): represents user A 
# # (B_SharedKey): represents user B 
# A_SharedKey = Ka * Y 
# print("A shared key :",compress(A_SharedKey)) 
# B_SharedKey = Kb * X 
# print("(B) shared key :",compress(B_SharedKey)) 
# print("Equal shared keys:", A_SharedKey == B_SharedKey)

############################################################################################################################

# # Import the required library
# from tkinter import *
# from tkinter import ttk

# # Create an instance of tkinter frame
# win=Tk()

# # Set the geometry
# win.geometry("700x350")

# def get_input():
#    label.config(text=""+text.get(1.0, "end-1c"))

# # Add a text widget
# text=Text(win, width=80, height=15)
# text.insert(END, "")
# text.pack()

# # Create a button to get the text input
# b=ttk.Button(win, text="Print", command=get_input)
# b.pack()

# # Create a Label widget
# label=Label(win, text="", font=('Calibri 15'))
# label.pack()

# win.mainloop()


###################################################################################################################################################

import tkinter 
from tkinter import ttk

