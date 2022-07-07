#checkboxların alt alta ve hizalı bir şekilde olması
from tkinter import *
pencere = Tk()
onay_pa = Checkbutton(text="Kubuntu")
onay_pa.place(relx = 0.0, rely = 0.1)
onay_de = Checkbutton(text="Debian")
onay_de.place(relx = 0.0, rely = 0.2)
onay_ub = Checkbutton(text="Ubuntu")
onay_ub.place(relx = 0.0, rely = 0.3)
onay_wix = Checkbutton(text="Windows XP")
onay_wix.place(relx = 0.0, rely = 0.4)
mainloop()
