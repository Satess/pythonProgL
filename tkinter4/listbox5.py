#ekle butonu ile entry bölümüne yazılan metni ekliyor.Entry bölümüne metin yazılmaz ise uyarı veriyor.Listeden eleman siliyor.
from tkinter import *
pencere = Tk()
liste = Listbox(bg="white")
liste.pack()
gnulinux_dagitimlari = ["Pardus", "Debian", "Ubuntu", "PclinuxOS", "TruvaLinux", "Gelecek Linux"]
for i in gnulinux_dagitimlari:
    liste.insert(END, i)
def yeni():
    global giris
    pencere2 = Toplevel()
    giris = Entry(pencere2)
    giris.pack()
    btn2 = Button(pencere2, text="tamam",command=ekle)
    btn2.pack()
def ekle():
    if not giris.get():
        giris.insert(END,"Veri Yok!")
    if not "Veri Yok!" in giris.get():
        liste.insert(END,giris.get())
        giris.delete(0,END)
def sil():
    liste.delete(ACTIVE)
etiket = Label(text="#################", fg="magenta", bg="light green")
etiket.pack()
btn = Button(text="ekle",bg="orange",fg="navy", command=yeni)
btn.pack()
btn_sil = Button(text="sil",command=sil)
btn_sil.pack()
etiket2 = Label(text="#################", fg="magenta", bg="light green")
etiket2.pack()
mainloop()

