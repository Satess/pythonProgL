#Bu araç bize pencereler üzerinde bir “liste içeren kutu” hazırlama imkanı veriyor.

from tkinter import *
pencere = Tk()
liste = Listbox()
liste.pack()
etiket = Label(text="#####################", fg="magenta", bg="light green")
etiket.pack()
btn = Button(text="ekle")
btn.pack()
etiket2 = Label(text="#####################", fg="magenta", bg="light green")
etiket2.pack()
mainloop()

