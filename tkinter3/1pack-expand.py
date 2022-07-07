from tkinter import *
pencere = Tk()
pencere.geometry("200x100")
nisan = Label(text="Nisan",
              fg = "white",
              bg = "red",
              font="Verdana 13 bold")
nisan.pack(expand=YES)
mayıs = Label(text="Mayıs",
             fg = "white",
             bg = "blue",
             font="Verdana 13 bold")
mayıs.pack(expand=YES)
haziran = Label(text="Haziran",
             fg = "white",
             bg = "green",
font="Verdana 13 bold")
haziran.pack(expand=YES)
mainloop()

