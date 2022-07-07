from tkinter import *  # modülü tanımladık
from PIL import ImageTk, Image

pencere = Tk()
pencere.geometry("800x900")  # penceremizin bouyutunu ayarladık
pencere.resizable(False, False)  # pencere büyütme özelliğini kapattık
pencere.tk_setPalette("#C43628")
pencere.title("DİKDÖRTGEN ÇEVRE/ALAN HESAPLAMA")  # başlığı yazdık


def cevre():
    etiket1["text"] = (int(yazi1.get())+int(yazi2.get())) * 2
    yazi1.delete(0,END)
    yazi2.delete(0, END)

def alan():
    etiket2["text"] = (int(yazi1.get())*int(yazi2.get())) # yazdığımız veriyi alıp işlem yapan fonksiyonu tanımladık
    yazi1.delete(0,END)
    yazi2.delete(0, END)

baslik = Label(text="DİKDÖRTGEN ÇEVRE/ALAN HESAPLAMA")  # yazı için etiket oluşturduk
baslik.pack()  # pencereye yerleştirdik

yazi1 = Entry(bg="white", fg="#C43628",font=("Times New Roman",20,"bold"))  # giriş için yer oluşturduk
yazi1.pack()  # pencereye yerleştirdik

yazi2 = Entry(bg="white", fg="#C43628",font=("Times New Roman",20,"bold"))  # giriş için yer oluşturduk
yazi2.pack()

buton1 = Button(text="ÇEVRE HESAPLA",command=cevre)  # hesaplamak için buton oluşturduk ve hazırladığımız fonksiyonu butona tanımladık
buton1.pack()  # pencereye yerleştirdik

buton2 = Button(text="ALAN HESAPLA",command=alan)
buton2.pack()

etiket1 = Label(text="Dikdörtgen Çevre Sonuç: ",fg="white",font=("Times New Roman",20,"bold"))  # sonuç için etiket oluşturduk
etiket1.pack()  # pencereye yerleştirdik

etiket2 = Label(text="Dikdörtgen Alan Sonuç: ",fg="white",font=("Times New Roman",20,"bold"))  # sonuç için etiket oluşturduk
etiket2.pack()


img = ImageTk.PhotoImage(Image.open('/Users/sates/Desktop/x_CfT61e_400x400.jpg'))
panel2 = Label(pencere, image = img,width=500, height=500)
panel2.pack()

buton3 = Button(pencere,text="ÇIKIŞ", command=pencere.destroy)
buton3.pack()

mainloop()  # kapanmaması için mainloop yazdık
