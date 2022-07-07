from tkinter import *
pencere = Tk()
etiket = Label(text="Asagıdaki kutucuga e.posta adresinizi yazınız!")
etiket.pack()
giris = Entry()
giris.pack()
cerceve = Frame(height=2, bd=5, relief=GROOVE)
cerceve.pack(side=LEFT)
dugme = Button(cerceve,text="Gönder",width=5,command=pencere.destroy)
dugme.pack(side=LEFT,padx=5)
dugme2 = Button(cerceve, text="Iptal", width=5,command=pencere.destroy)
dugme2.pack()
mainloop()

#------------------NESNE TAB VERSİYON------------------
from tkinter import *
class Uygulama(object):
    def __init__(self):
        self.guiPenAr()

    def guiPenAr(self):
        self.etiket = Label(text="A ̧sa ̆gıdaki kutucu ̆ga e.posta adresinizi yazınız!")
        self.etiket.pack()
        self.giris = Entry()
        self.giris.pack()
        self.cerceve = Frame()
        self.cerceve.pack(side=BOTTOM,
                          padx=5,
                          pady=5)
        self.dugme = Button(self.cerceve, text="Gönder",
                            width=5, command=pencere.destroy)
        self.dugme.pack(side=LEFT,padx=5)
        self.dugme2 = Button(self.cerceve,text="Iptal",width=5)
        self.dugme2.pack()
pencere = Tk()
uyg = Uygulama()
mainloop()