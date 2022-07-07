from tkinter import *
pencere = Tk()
etiket = Label(text="Aşağ̆ıdaki kutucuga e.posta adresinizi yazınız!")
etiket.pack()
giris = Entry()
giris.pack()
cerceve = Frame(height=2, bd=10, relief=SUNKEN)
cerceve.pack(fill=X, pady=5, padx=5)
dugme = Button(text="Gönder", command=pencere.destroy)
dugme.pack()
mainloop()

#---------NESNE TAB VERSİYON------------
from tkinter import *
class Uygulama(object):
    def __init__(self): self.guiPenAr()
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
