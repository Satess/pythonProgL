from tkinter import * 
pencere = Tk()
def olustur():
    dosya = open("14022-2.txt", "w")
dugme = Button(text = "olustur", command=olustur)
dugme.pack()
dugme2 = Button(text = "çıkıs", command=pencere.quit)
dugme2.pack()
mainloop()