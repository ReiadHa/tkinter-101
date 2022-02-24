import random
import tkinter as tk 

#================================================ lijsten zitten hier onder===========================
lijst = ['Gaming Pc','Gaming laptop','Gaming muis','Gaming Keyboard','4k scherm 32 inch']
listt = """
De Prijzen zijn:
Gaming Pc
Gaming laptop
Gaming muis
Gaming Keyboard
4k scherm 32 inch
"""
#============================ tkinter en varibales setup ===========================================
counter = 0
window = tk.Tk()
window.title('Grabbelton')
window.config(bg='grey')
button1 = tk.Button(text='klik hier om een prijs te grabbelen', bg="black", fg="white")
stringvar = tk.StringVar(value=listt)
window.geometry('300x300')
label1 = tk.Label(
    button1.pack(side=tk.TOP),
)
label1.config(textvariable=stringvar,bg='grey')
label1.place(relx = 0.5,rely = 0.5,anchor = 'center',)

#================================================functies hier onder=============================
def click():
    global counter
    if len(lijst) != 0:
        counter += 1
        root = tk.Tk()
        root.title(f'Prijz nummer :{counter}')
        root.config(bg='grey')
        root.geometry('300x300')
        rand = random.choice(lijst)
        lijst.remove(rand)
        label2 = tk.Label(
            root,
            text =f'Gefeliciteerd! Jou prijz is:\n {rand}',
            bg='grey'
        )
        label1.config(bg='grey')
        label2.place(relx = 0.5,rely = 0.5,anchor = 'center')
    elif len(lijst) == 0:
        window2 = tk.Tk()
        window2.geometry('350x300')
        window2.config(bg='grey')
        window2.title('Prijzen zijn op!')
        win2Label = tk.Label(
            window2,
            text='Sorry er zij geen Prijzen meer :(',
            font=("Terminal", 15)
        )
        win2Label.place(relx = 0.5,rely = 0.5,anchor = 'center',)


button1.config(command=click)
window.mainloop()

