


import sqlite3

baglanti= sqlite3.connect('/Users/sates/Desktop/okul.db')
isaretci=baglanti.cursor()
# hepsinin telefon numarasını değiştirdik
db=isaretci.execute('UPDATE ogrenciler SET telefon_numarasi="12345678912" WHERE telefon_numarasi="222222222"')
db=isaretci.execute('SELECT * FROM ogrenciler WHERE telefon_numarasi="12345678912" ')
print(db.fetchall())

baglanti.commit()



