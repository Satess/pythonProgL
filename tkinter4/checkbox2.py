#checkboxları yan yana sıralama
from tkinter import *
pencere = Tk()
onay_el = Checkbutton(text="elma")
onay_el.pack(side=LEFT)
onay_sa = Checkbutton(text="salatalık")
onay_sa.pack(side=RIGHT)
onay_do = Checkbutton(text="domates")
onay_do.pack(side=LEFT)
onay_ka = Checkbutton(text="karnıbahar")
onay_ka.pack(side=LEFT)
mainloop()


