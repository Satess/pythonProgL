#Adından da anlasılacağı gibi bu araç bize pencerelerimiz üzerinde menüler hazırlama olanagı sağlıyor...

from tkinter import *
pencere = Tk()
menu = Menu(pencere)
pencere.config(menu=menu)
dosya = Menu(menu)
menu.add_cascade(label="Dosya",menu=dosya)
dosya.add_command(label="Aç")
dosya.add_command(label="Kaydet")
dosya.add_command(label="Farklı Kaydet...")
dosya.add_command(label="Çıkıs",command=pencere.quit)
mainloop()

