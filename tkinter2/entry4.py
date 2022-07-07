from tkinter import *
import random

pencere = Tk()

def bas():
    a = random.randint(1, 10)
    giris.delete(0, END)
    giris.insert(0, a)

giris = Entry(width=10)
giris.pack()

dugme = Button(text="bas", command=bas, width=2, height=0)
dugme.pack()
mainloop()

#Bunlar, “width” ve “height” adlı seçenekler...
# “width” seçeneği yardımıyla bir pencere aracının genişligini; “height” seçenegi yardımıyla ise o aracın
# yüksekliğini belirliyoruz.