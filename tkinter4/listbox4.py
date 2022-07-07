#ekle düğmesine basıldığında ayrı bir pencere açılsın ve kullanıcıdan girdi
# alarak ana penceredeki liste kutusuna eklesin...

from tkinter import *
pencere = Tk()
liste = Listbox(bg="white")
liste.pack()
liste2 = ["Pardus", "Debian", "Ubuntu", "PclinuxOS", "TruvaLinux", "Gelecek Linux"]
for i in liste2:
    liste.insert(END, i)
def yeni():
    global giris
    pencere2 = Toplevel()
    giris = Entry(pencere2)
    giris.pack()
    btn2 = Button(pencere2, text="tamam",command=ekle)
    btn2.pack()
def ekle():
    liste.insert(END,giris.get())#kullanıcının yazdığı bilgiyi ekliyor.
    giris.delete(0,END)#ekleme işleminden sonra siliyor.
etiket = Label(text="#################", fg="magenta", bg="light green")
etiket.pack()
btn = Button(text="ekle", command=yeni)
btn.pack()
etiket2 = Label(text="#################", fg="magenta", bg="light green")
etiket2.pack()

mainloop()


