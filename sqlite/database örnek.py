import sqlite3, os
from datetime import date
conn = sqlite3.connect('STest.db')
db = 'Test.db'
if not os.path.isfile(db):
    print('Böyle bir veritabanına erişilemedi.')
else:
    print('Veritabanına başarıyla erişim sağlandı.')

c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS stok (
    urunid INTEGER PRIMARY KEY AUTOINCREMENT,
    urunad TEXT,
    urunmiktar INTEGER,
    uruntarih DATe,
    urunfiyat INTEGER
)""")
while True:
    secim = int(input("""**************************************************
Veri eklemek için 1
Veri görüntülemek için 2 rakamlarını tuşlayınız:
**************************************************\n:  """))
    if secim == 1:
            uruntarih=date.today()
            urunad = input("Urun Ad :")
            urunfiyat= input("Ürün Fiyatı :")
            urunmiktar = input("Ürün Miktarı: ")

            c.execute("INSERT INTO stok(urunad,urunfiyat,uruntarih,urunmiktar) VALUES (?,?,?,?)",(urunad,urunfiyat,uruntarih,urunmiktar))

    elif secim == 2:
            c.execute("Select * from stok")
            data = c.fetchall()
            #Eğer belirli miktarda veri getireceksek fetchmany metodunu kullanabiliriz.
            #datamany = c.fetchmany(2)
            print(data)
            print('\n')

    else :
       print("Lütfen menüdeki değerleri tuşlayınız..")
    conn.commit()

conn.close()