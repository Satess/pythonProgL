from tkinter import *
pencere = Tk()
ekim = Label(text="Ekim",
              fg = "white",
              bg = "red",
              font="Verdana 13 bold")
ekim.pack(side=TOP)
kasim = Label(text="Kasım",
             fg = "white",
             bg = "blue",
             font="Verdana 13 bold")
kasim.pack(side=BOTTOM)
aralik = Label(text="Aralık",
             fg = "white",
             bg = "green",
font="Verdana 13 bold")
aralik.pack(side=LEFT)
mainloop()

