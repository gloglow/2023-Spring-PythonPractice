import tkinter as tk

window=tk.Tk()
canvas=tk.Canvas(window, width=600, height=600)
canvas.grid(row=0, column=0)

for _ in range(15):
    canvas.create_line(0, _*40, 600, _*40, fill='black')
    canvas.create_line(_*40, 0, _*40, 600, fill='black')

window.mainloop()