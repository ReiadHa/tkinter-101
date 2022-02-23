import tkinter as tk
from time import strftime

window = tk.Tk()
window.title('clock')
window.geometry('300x100')

label1 = tk.Label(
    window,
    font=("Terminal", 25),
    bg= 'lightblue',
    fg= 'darkred'
    )
label1.pack()
def tijd1():
    tijd = strftime('%H:%M:%S %p')
    stringVAr = tk.StringVar(value=tijd)
    label1.config(textvariable=stringVAr)

    window.after(1000,tijd1)

tijd1()

window.mainloop()


