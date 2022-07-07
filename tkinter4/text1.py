
from tkinter import *
pencere= Tk()
metin= Text(fg = "blue",font="Helvetica 13 bold")
metin.insert(END,"Sürüm 0.1.1")
metin.insert(END,'''ArgumentParser() nesnesi varsayılan olarak komut satırından 
okuduğu değerleri karakter dizisi (string) olarak alır. 
Bazı durumlarda farklı tiplerde değişkenlere ihtiyaç duyarız. 
Bunun için type kullanılır. Şimdi uygulamamızı çalıştırdığımız dizine args
.txt dosyası oluşturalım ve kodumuzu çalıştıralım. Kod:''')
metin.pack()
mainloop()



