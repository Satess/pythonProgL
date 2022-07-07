
from tkinter import *
pencere = Tk()
def ekle():
    pencere2 = Toplevel()
    btn_pen = Button(pencere2,text="çıkıs", command=pencere2.destroy)
    btn_pen.pack()
btn_pen2 = Button(pencere,text="ekle", command=ekle)
btn_pen2.pack()
mainloop()



