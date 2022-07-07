
import sqlite3

baglanti= sqlite3.connect('/Users/sates/Desktop/okul.db')
isaretci=baglanti.cursor()

db=isaretci.execute('SELECT * FROM ogrenciler WHERE sinif LIKE "Hazırlık%"')
print(db.fetchall())
#% herhangi bir karakter anlamındadır.

baglanti.commit()



