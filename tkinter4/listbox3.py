from tkinter import *
pencere = Tk()
liste = Listbox(bg="white")
liste.pack()
liste2 = ["Pardus", "Debian", "Ubuntu", "PclinuxOS", "TruvaLinux", "Gelecek Linux"]
for i in liste2:#listedeki elemanları for döngüsü ile ekliyoruz.
    liste.insert(END, i)
etiket = Label(text="#################", fg="magenta", bg="light green")
etiket.pack()
btn = Button(text="ekle")
btn.pack()
etiket2 = Label(text="#################", fg="magenta", bg="light green")
etiket2.pack()
mainloop()


