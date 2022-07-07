from tkinter import *
pencere = Tk()
pencere.geometry("200x100")
temmuz = Label(text="Temmuz",
              fg = "white",
              bg = "red",
              font="Verdana 13 bold")
temmuz.pack(expand=YES, fill = X)
agustos = Label(text="Ağustos",
             fg = "white",
             bg = "blue",
             font="Verdana 13 bold")
agustos.pack(expand=YES, fill = Y)
eylul = Label(text="Eylül",
             fg = "white",
             bg = "green",
font="Verdana 13 bold")
eylul.pack(expand=YES, fill = BOTH)
mainloop()

