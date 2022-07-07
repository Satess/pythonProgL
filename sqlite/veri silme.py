


import sqlite3
#veri silmek için DELETE ifadesini kullanılıyoruz.
baglanti= sqlite3.connect('/Users/sates/Desktop/okul.db')
isaretci=baglanti.cursor()

db=isaretci.execute('DELETE FROM ogrenciler WHERE adi="Esin"')

print(db.fetchall())

baglanti.commit()
baglanti.close()


