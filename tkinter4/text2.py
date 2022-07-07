from tkinter import *
pencere= Tk()
a= "Sürüm 0.1.1"
metin= Text(bg="orange",fg = "blue",font="Helvetica 13 bold")
metin.insert(END,a.center(112,"*"))#metni 112 yıldızın merkezine yerleştiriyor.
metin.pack()
mainloop()


