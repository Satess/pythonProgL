#verileri alırken belirli bir alana göre sıralayabiliriz.
#ORDEY BY  İFADESİ İLE YAPILIR.


import sqlite3

baglanti= sqlite3.connect('/Users/sates/Desktop/okul.db')
isaretci=baglanti.cursor()

db=isaretci.execute('SELECT adi,soyadi,telefon_numarasi FROM ogrenciler ORDER BY adi')
print(db.fetchmany(2))

baglanti.commit()




