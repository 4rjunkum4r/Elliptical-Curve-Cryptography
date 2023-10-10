d to execute both windows
    os.system('python '+filename)


gen_btn = tk.Button(
    mainframe,
    text="CLICK HERE TO GENERATE THE KEY PAIR",
    cursor="pirate",
    background='Black',
    foreground='White',
    border=5, font=("Cambria", 10, "bold"), command=lambda: open("Key.py"))
gen_btn.grid(row=1, column=0)

seperator = tk.Label(mainfram