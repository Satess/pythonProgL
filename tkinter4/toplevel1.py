
from tkinter import *
pencere = Tk()
def ekle():
    pencere2 = Toplevel()
    pencere2.title("ikinci pencere")

btn_pen2 = Button(text="ekle", command=ekle)
btn_pen2.pack()
mainloop()


