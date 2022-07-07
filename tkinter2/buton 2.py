from tkinter import *
pencere = Tk()
def olustur():
    dosya = open("hza.txt","w")#dosya oluşturma

buton = Button(text = " DOSYA OLUŞTUR", command=olustur)
buton.pack()
mainloop()  


