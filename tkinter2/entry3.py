from tkinter import *
pencere = Tk()

def olustur():
    dosya = open("hz18subat.txt","w")#bu şekilde kullanıcıdan veri alabiliriz.
    metin = giris.get()
    dosya.write(metin)

giris = Entry()
giris.pack()

dugme = Button(text = "OLUSTUR", command = olustur)
dugme.pack(side=LEFT)

dugme2 = Button(text = "ÇIK", command = pencere.quit)
dugme2.pack(side=RIGHT)

mainloop()

#Burada da bize yabancı olan tek ifade “giris.get()”...
# Bu ifade “Entry” pencere aracı ile kul- lanıcıdan aldıg ̆ımız metni elimizde tutup saklamamızı sağlıyor.

#Burada bu ifadeyi önce “metin” adlı bir degis ̧kene atadık, sonra da bu metin degis ̧keninin içerigini
# “dosya.write(metin)” komu- tunun yardımıyla bos ̧ bir dosyaya aktardık.