
from tkinter import *
pencere= Tk()
def al():
    a= metin.get("sel.first","sel.last")
    metin2.insert(END,a)
metin= Text(height=10,width=35,bg="white",fg ="blue",font="Helvetica 13 bold")
metin.pack()
metin2= Text(height=10,width=50, bg="black",fg="white")
metin2.pack()
btn= Button(text="al",command=al)
btn.pack()
mainloop()


