import tkinter as tk
from turtle import position

window = tk.Tk()
window.title('Hello')
window.geometry('300x300')
label1 = tk.Label(
    window,
    text = 'Hello \nTkinter!',
    bg='green',
    fg= 'yellow',
    font=("Helvetica", 30),
    width=10,
    height=2,
    
)


label1.place(
    relx = 0.5,
    rely = 0.5,anchor = 'center'
)

window.mainloop()
