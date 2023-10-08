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

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('My Window')
window.geometry('100x100')

frame = tk.Frame(window)
frame.pack()

l = tk.Label(frame, bg='white', width=20, text='Select')
l.pack()

def print_selection(event):
    option_selected = var.get()
    if option_selected == "Python":
        l.config(text='I love Python')
    elif option_selected == "C++":
        l.config(text='I love C++')
    else:
        l.config(text='Select')

var = tk.StringVar()
combobox = ttk.Combobox(frame, textvariable=var, values=["Python", "C++"], state='readonly')
combobox.current(0)

# Bind the `print_selection()` function to the `<<ComboboxSelected>>` event.
combobox.bind("<<ComboboxSelected>>", print_selection)
combobox.pack()

window.mainloop()