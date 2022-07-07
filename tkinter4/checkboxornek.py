#get()---Bu ifade yardımıyla bir değiş̧keninin degerini sonradan kullanmak üzere depolayabiliyoruz.


from tkinter import *
pencere = Tk()
# Onay kutusu için bir deği̧sken olu̧sturuyoruz
v = IntVar()
# Bu degi̧skene deger olarak "0" atayalım
v.set(0)
# Öbür onay kutusu için ba̧ska bir değisken daha olu̧sturuyoruz
z = IntVar()
# Bu degi̧skene de "0" değerini atıyoruz.
z.set(0)
# Bu kez bir karakter deği̧skeni olu̧sturalım
d = StringVar()
# Bu degi̧skenin degeri "Kubuntu" olsun.
d.set("Kubuntu")
# Bir tane daha karakter degiskeni olusturalım
e = StringVar()
# Bunun da degeri "Debian" olsun.
e.set("Debian")
#̧Simdi onay kutularını seçili hale getirdigimizde çalı̧smasını #istediğimiz komut için bir fonksiyon olu̧sturuyoruz:
def onay():
# Eger "v" deği̧skeninin değeri "1" ise....
    if v.get() == 1:
        # d.get() ile "d" deği̧skeninin değerini alıyoruz...
        giris.insert(0,"Merhaba %s kullanıcısı" %d.get())
        # Yok eğer "z" deği̧skeninin değeri "1" ise...
    elif z.get() == 1:
        giris.delete(0,END)
        # e.get() ile "e" deği̧skeninin değerini alıyoruz...
        giris.insert(0,"Merhaba %s kullanıcısı" %e.get())
            # Deği̧skenlerin değer "1" degil, ba̧ska bir değer ise..."
    else:
        giris.delete(0,END)
# Asağıda "text" seçeneginin değerinin "d.get()" olduğuna dikkat edin.
onay1 = Checkbutton(text=d.get(), variable=v, command=onay)
onay1.place(relx = 0.0, rely = 0.1)
# Aşagıda "text" seçeneginin degerinin "e.get()" olduguna dikkat edin.
onay2 = Checkbutton(text=e.get(), variable=z, command=onay)
onay2.place(relx= 0.0, rely= 0.2)

giris = Entry(width=24)
giris.place(relx = 0.0, rely=0.0)
mainloop()