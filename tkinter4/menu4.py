
from tkinter import *
pencere= Tk()
menu= Menu(pencere)
pencere.config(menu=menu)
dosya= Menu(menu, tearoff=0)
menu.add_cascade(label="Dosya",menu=dosya)
dosya.add_command(label="Aç")
dosya.add_command(label="Kaydet")
dosya.add_command(label="Farklı Kaydet...")
dosya.add_command(label="Çıkıs ̧",command=pencere.quit)
yeni= Menu(dosya,tearoff=0)
dosya.add_cascade(label="Yeni",menu=yeni)
yeni.add_command(label="Metin Belgesi")
yeni.add_command(label="Resim Dosyası")
yeni.add_command(label="pdf dokümanı")
dosya2= Menu(menu,tearoff=0)
menu.add_cascade(label="Düzen",menu=dosya2)
dosya2.add_command(label="Bul")
mainloop()


