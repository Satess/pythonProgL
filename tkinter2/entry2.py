from tkinter import *
pencere = Tk()


def sil():
    giris.delete(0,END)
#“giris.delete(0, END)”. Bu komut, görünüşünden de anlaşılacağı gibi,
# “giris” degiskenininiçerigini silmeye yarıyor.

#Parantez içindeki “0, END” ifadesi, metin kutusuna girilen kelimenin en basından en sonuna kadar
# bütün harflerin sil- inmesi emrini veriyor. Eger “0, END” yerine, mesela “2, 4” gibi bir ifade koysaydık,
# girilen kelimenin 2. harfinden itibaren 4. harfine kadar olan kısmın silinmesi emrini vermis ̧ olacaktık.

giris = Entry()
giris.pack()

buton1= Button(text = "KAPAT", command = pencere.quit)
buton1.pack(side = LEFT)

buton2= Button(text = "SIL", command = sil)
buton2.pack(side = RIGHT)


mainloop()