from tkinter import *
pencere = Tk()
d = IntVar()
d.set(1)
btn1 = Checkbutton(text="Kubuntu", variable=d)
btn1.place(relx=0.0,rely=0.1)

e = IntVar()
e.set(0)
btn2 = Checkbutton(text="Win", variable=e)
btn2.place(relx=0.3,rely=0.3)

mainloop()

