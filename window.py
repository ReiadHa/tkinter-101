from time import sleep
import tkinter as tk
from threading import Timer

#======================= lijst en window setup ==========
window = tk.Tk()
window.title('window test')
counter = 6
sizeKleur = {
    '50x50'   :'purple',
    '100x100' :'red',
    '150x150' :'blue',
    '200x200' :'green',
    '250x250' :'yellow',
    '300x300' :'black',
}
#========================functions hieronder===============================
def test():
    global counter
    for s in sizeKleur:
        window.geometry(s)
        window.config(bg=sizeKleur[s])
        print(f'test {counter}')
        counter -= 1
        sleep(2)
        if sizeKleur[s] == 'black':
            print('Boom!')
            window.destroy()
Timer(0, test).start()


    
window.mainloop()




