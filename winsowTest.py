import tkinter as tk

window = tk.Tk()

colors = ['white','black','green','yellow','blue','purple']
size   = 0
counter = 0
def changeColor():
    global size,counter
    index = int((size/50))
    if index == len(colors):
        print('Boom!')
        window.destroy()
    else:
        counter += 1
        size += 50
        window.config(bg=colors[index])
        window.geometry(f'{size}x{size}')
        window.after(2000,changeColor)
        print(f'test {counter}')
changeColor()
window.mainloop()