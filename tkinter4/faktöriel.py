

from tkinter import *  # modülü tanımladık
#from PIL import ImageTk, Image

pencere = Tk()
pencere.geometry("500x500")  # penceremizin bouyutunu ayarladık
pencere.resizable(False, False)  # pencere büyütme özelliğini kapattık
pencere.tk_setPalette("black")
pencere.title("FAKTÖRİYEL HESABI")  # başlığı yazdık


def onay():
    sonuc=1
    a=yazi1.get()
    a=int(a)
    while a>1:
        sonuc*=a
        a-=1
    etiket1["text"] =sonuc
    yazi1.delete(0,END)


baslik = Label(text="FAKTÖRİYEL HESABI",font=("Times New Roman",30,"bold"))# yazı için etiket oluşturduk
baslik.pack()  # pencereye yerleştirdik

yazi1 = Entry(bg="#E9E13A", fg="black",font=("Times New Roman",20,"bold"))  # giriş için yer oluşturduk
yazi1.pack()  # pencereye yerleştirdik
buton1 = Button(text="HESAPLA",
               command=onay)  # hesaplamak için buton oluşturduk ve hazırladığımız fonksiyonu butona tanımladık
buton1.pack()  # pencereye yerleştirdik

buton2 = Button(pencere,text="ÇIKIŞ", command=pencere.destroy)
buton2.pack(expand=YES)

etiket1 = Label(text="SONUÇ: ",
                fg="white",
                bg="Black",
                font=("Times New Roman",20,"bold"))

# sonuç için etiket oluşturduk
etiket1.pack()  # pencereye yerleştirdik


mainloop()  # kapanmaması için mainloop yazdık
