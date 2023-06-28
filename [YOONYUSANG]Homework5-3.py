import tkinter as tk
import winsound

global memory_num, memory_ope
memory_num=0
memory_ope=''

def button_number(n):
    label.configure(text=label.cget('text')*10+n)

def button_func(n):
    global memory_num, memory_ope
    if n=='=':
        light_1.configure(fill='black')
        winsound.Beep(frequency=440, duration=1000)
        if memory_ope=='':
            return
        else:
            if memory_ope=='+':
                label.configure(text=memory_num+label.cget('text'))
            elif memory_ope=='-':
                label.configure(text=memory_num-label.cget('text'))
            elif memory_ope=='*':
                label.configure(text=memory_num*label.cget('text'))
            elif memory_ope=='/':
                label.configure(text=memory_num/label.cget('text'))
            memory_num=0
            memory_ope=''
    elif n=='CE':
        label.configure(text=0)
        memory_num=0
        memory_ope=''
    else:
        memory_num=label.cget('text')
        label.configure(text=0)
        if n=='+':
            memory_ope='+'
        elif n=='-':
            memory_ope='-'
        elif n=='*':
            memory_ope='*'
        elif n=='/':
            memory_ope='/'
    



window=tk.Tk()
window.title("Calculater")

label=tk.Label(window, text=0, width=30, height=10)
canvas=tk.Canvas(window, width=800, height=150)
light_1=canvas.create_oval(100,50,150,100, fill='red')

b1=tk.Button(window, text='1', width=10, height=5, command=lambda:button_number(1))
b2=tk.Button(window, text='2', width=10, height=5, command=lambda:button_number(2))
b3=tk.Button(window, text='3', width=10, height=5, command=lambda:button_number(3))
b4=tk.Button(window, text='4', width=10, height=5, command=lambda:button_number(4))
b5=tk.Button(window, text='5', width=10, height=5, command=lambda:button_number(5))
b6=tk.Button(window, text='6', width=10, height=5, command=lambda:button_number(6))
b7=tk.Button(window, text='7', width=10, height=5, command=lambda:button_number(7))
b8=tk.Button(window, text='8', width=10, height=5, command=lambda:button_number(8))
b9=tk.Button(window, text='9', width=10, height=5, command=lambda:button_number(9))
b0=tk.Button(window, text='0', width=10, height=5, command=lambda:button_number(0))
b_CE=tk.Button(window, text='CE', width=10, height=5, command=lambda:button_func('CE'))
b_pls=tk.Button(window, text='+', width=10, height=5, command=lambda:button_func('+'))
b_min=tk.Button(window, text='-', width=10, height=5, command=lambda:button_func('-'))
b_mul=tk.Button(window, text='*', width=10, height=5, command=lambda:button_func('*'))
b_div=tk.Button(window, text='/', width=10, height=5, command=lambda:button_func('/'))
b_rst=tk.Button(window, text='=', width=10, height=5, command=lambda:button_func('='))


label.grid(row=0, column=0, columnspan=4)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b7.grid(row=4, column=0)
b8.grid(row=4, column=1)
b9.grid(row=4, column=2)
b0.grid(row=4, column=3)
b_CE.grid(row=2, column=3)
b_pls.grid(row=1, column=0)
b_min.grid(row=1, column=1)
b_mul.grid(row=1, column=2)
b_div.grid(row=1, column=3)
b_rst.grid(row=3, column=3)
canvas.grid(row=5,column=5, columnspan=5)

window.mainloop()