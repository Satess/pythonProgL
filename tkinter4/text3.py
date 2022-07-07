
from tkinter import *
pencere= Tk()
def al():
    a= metin.get(0,END)
    giris.insert(1.0, a)
metin= Text()
metin.pack()
btn= Button(text="al", command=al)
btn.pack()
giris= Entry()
giris.pack()
mainloop()


