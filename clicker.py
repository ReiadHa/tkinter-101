import tkinter as tk 
#=================== funtions hier onder=================================
def up():
    global number
    number += 1
    print(number)
    clicker()
def down():
    global number
    number -= 1
    print(number)
    clicker()
def clicker():
    global number,lab
    if number < 0:
        win.config(bg='red')
    elif number > 0 :
        win.config(bg='green')
    elif number == 0:
        win.config(bg='grey')
    labstr = tk.StringVar(value=f'{number}')
    lab.config(textvariable=labstr)

#==================== window/labels/buttons setup hieronder====================

number = 0
win = tk.Tk()
win.geometry('300x150')
lab = tk.Label( text= f'{number}',width=20)
lab.config(bg='white')
button1 = tk.Button(text='Up',width=20)
button2 = tk.Button(text='Down',width=20)
lab.place(anchor='center',relx=0.5,rely = 0.5)
button1.pack(side=tk.TOP)
button2.pack(side=tk.BOTTOM)
button1.config(command=up)
button2.config(command=down)


clicker()

#=====window mainloop========
win.mainloop()