
import sqlite3

baglanti= sqlite3.connect('/Users/sates/Desktop/3.db')
isaretci=baglanti.cursor()

#db=isaretci.execute('ALTER TABLE ogrenciler RENAME TO aile')
#ikinci kez isim değiştirmede hata veriyor çünkü isim değiştiğinden önceki tabloyu bulamıyor.

db=isaretci.execute('SELECT name FROM sqlite_master')
print(db.fetchall())
s=isaretci.execute('PRAGMA TABLE_INFO(ogrenciler)')
for i in s.fetchall():
    print(i[1],i[2])
baglanti.commit()