from tkinter import *  # modülü tanımladık
#from PIL import ImageTk, Image

pencere = Tk()
pencere.geometry("300x470")  # penceremizin bouyutunu ayarladık
pencere.resizable(True,True)  # pencere büyütme özelliğini kapattık
pencere.tk_setPalette("black")
pencere.title("ÜÇGEN ÇEVRE HESABI")  # başlığı yazdık



def cevre():
    if abs(int(yazi2.get())-int(yazi3.get()))<int(yazi1.get())<int(yazi2.get())+int(yazi3.get()) and abs(int(yazi1.get())-int(yazi3.get()))<int(yazi2.get())<int(yazi1.get())+int(yazi3.get()) and abs(int(yazi1.get())-int(yazi2.get()))<int(yazi3.get())<int(yazi1.get())+int(yazi2.get()):
        etiket1["text"] = (int(yazi1.get())+int(yazi2.get())+int(yazi3.get()))
        yazi1.delete(0,END)
        yazi2.delete(0, END)
        yazi3.delete(0,END)
    else:
        etiket1["text"] ='''Üçgen oluşturamıyor...'''
        yazi1.delete(0, END)
        yazi2.delete(0, END)
        yazi3.delete(0, END)



baslik = Label(text="ÜÇGEN ÇEVRE HESAPLAMA")  # yazı için etiket oluşturduk
baslik.pack(expand=YES)  # pencereye yerleştirdik

yazi1 = Entry(bg="#04769B", fg="white",font=("Times New Roman",20,"bold"))  # giriş için yer oluşturduk
yazi1.pack(expand=YES)  # pencereye yerleştirdik

yazi2 = Entry(bg="#04769B", fg="white",font=("Times New Roman",20,"bold"))  # giriş için yer oluşturduk
yazi2.pack(expand=YES)

yazi3 = Entry(bg="#04769B", fg="white",font=("Times New Roman",20,"bold"))  # giriş için yer oluşturduk
yazi3.pack(expand=YES)

buton1 = Button(text="ÇEVRE HESAPLA",
               command=cevre)  # hesaplamak için buton oluşturduk ve hazırladığımız fonksiyonu butona tanımladık
buton1.pack(expand=YES)  # pencereye yerleştirdik

buton2 = Button(text="ÇIKIŞ", command=pencere.destroy)
buton2.pack(expand=YES)

etiket1 = Label(text="Üçgen Çevre Sonuç: ",fg="white",font=("Times New Roman",15,"bold"))  # sonuç için etiket oluşturduk
etiket1.pack(expand=YES)  # pencereye yerleştirdik

mainloop()  # kapanmaması için mainloop yazdık
