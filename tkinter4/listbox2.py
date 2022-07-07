from tkinter import *
pencere = Tk()
liste = Listbox(bg="black", fg="white")
liste.insert(END,"KARİNA")#eleman ekleme
liste.insert(END,"CAPELLA")
liste.insert(END,"RİGEL")
liste.insert(END,"REGULUS")
liste.insert(0,"SİRİUS")
liste.pack()
etiket = Label(text="#####################", fg="magenta", bg="light green")
etiket.pack()
btn = Button(text="ekle")
btn.pack()
etiket2 = Label(text="#####################", fg="magenta", bg="light green")
etiket2.pack()
mainloop()

