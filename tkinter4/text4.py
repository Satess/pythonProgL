from tkinter import *
pencere= Tk()
def al():
    metin2.insert(END,metin.get(2.0,END))
a= "Sürüm 0.1.1"
metin= Text(height=15,bg="black",fg = "white",font="Helvetica 13 bold")
metin.insert(END,a.center(112,"*"))
metin.pack()
metin2= Text(height=15,width=115, bg="light blue",fg="red")
metin2.pack()
btn= Button(text="al",command=al)
btn.pack()
mainloop()


