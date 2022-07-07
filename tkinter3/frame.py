from tkinter import *
pencere = Tk()
yeni = Frame(height=2, bd=10, relief=SUNKEN)
yeni.pack(side=BOTTOM)
uyari = Label(pencere,text="Programdan çıkmak istediginize emin misiniz?")
uyari.pack()
evet = Button(yeni,text="Evet",command=pencere.quit)
evet.pack(side=LEFT)
hayir = Button(yeni,text="Hayır")
hayir.pack()
mainloop()


