import sqlite3

baglanti= sqlite3.connect('/Users/sates/Desktop/1.db')
isaretci=baglanti.cursor()


s=isaretci.execute('''INSERT INTO ogrenciler(ogrenci_no,adi,soyadi,cinsiyeti,sinif,
telefon_numarasi,velisi,dogum_yeri) VALUES (27,'Kübra','Aktaş','K','HazırlıkA','111111111','Mehmet',
'Ankara')''')

print(s.lastrowid)

baglanti.commit()
