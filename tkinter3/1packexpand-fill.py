from tkinter import *
pencere = Tk()
dolar = Label(text="Dolar",
              fg = "white",
              bg = "red",
              font="Verdana 13 bold")
dolar.pack(side=TOP, expand=YES,fill=BOTH)
avro = Label(text="Avro",
             fg = "white",
             bg = "blue",
             font="Verdana 13 bold")
avro.pack(side=TOP,expand=YES, fill=BOTH)
lira = Label(text="Lira",
             fg = "white",
             bg = "green",
font="Verdana 13 bold")
lira.pack(side=TOP,expand=YES, fill=BOTH)
mainloop()


