#tablo adını  değiştirme
#tabloya alan ekleme işlemlerini yapabiliyoruz.

import sqlite3

baglanti= sqlite3.connect('/Users/sates/Desktop/4.db')
isaretci=baglanti.cursor()

#db=isaretci.execute('ALTER TABLE ogrenciler RENAME TO aile')
#ikinci kez isim değiştirmede hata veriyor çünkü isim değiştiğinden önceki tabloyu bulamıyor.

db=isaretci.execute('ALTER TABLE aile ADD dogum_tarihi FLOAT')
baglanti.commit()