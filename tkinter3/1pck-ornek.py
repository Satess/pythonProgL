from tkinter import *
pencere = Tk()
uyari = Label(text="Programdan çıkmak istediginize emin misiniz?")
uyari.pack(side=TOP)
evet = Button(text="Evet",command=pencere.quit)
evet.pack(side=LEFT)
hayir = Button(text="Hayır")
hayir.pack(side=RIGHT)
mainloop()

