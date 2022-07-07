
from tkinter import *
pencere = Tk()
def olustur():
    dosya = open("deneme.txt", "w")
dugme = Button(text = "olustur", command=olustur)
dugme.pack()
dugme2 = Button(text = "çıkıs", command=pencere.quit)
dugme2.pack()
mainloop()
