import tkinter as tk

def button_red_clicked():
    label.configure(background='red')

def button_blue_clicked():
    label.configure(background='blue')


window=tk.Tk()

label=tk.Label(window, width=10, height=10)
button_red=tk.Button(window, text='Red', width=10, height=10, command=button_red_clicked)
button_blue=tk.Button(window, text='blue', width=10, height=10, command=button_blue_clicked)

label.grid(row=0, column=1)
button_red.grid(row=1, column=0)
button_blue.grid(row=1, column=2)

window.mainloop()