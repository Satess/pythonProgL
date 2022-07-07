#veriler INSERT INTO  komutu ile girilir.
import sqlite3
baglanti= sqlite3.connect('/Users/sates/Desktop/hza.db')
isaretci=baglanti.cursor()

s=isaretci.execute('''INSERT INTO ogrenciler(ogrenci_no,adi,soyadi,cinsiyeti,sinif,
telefon_numarasi,velisi,dogum_yeri) VALUES (27,'Şeyma','Ateş','K','HazırlıkE','5444586070545','Mehmet',
'Kahramanmaraş')''')

a=isaretci.execute('''INSERT INTO ogretmenler(kayit_no,adi,soyadi,brans,telefon_no,hizmet_puanı) VALUES 
(22,'CEREN','AKTAS','ingilizce','00000000000',200)''')

b=isaretci.execute(''' INSERT INTO okul_bilgileri(id,ad,kurulus_tarihi,adres,kontenjan,telefon) VALUES 
(12345,'Beşiktaş Anadolu Lisesi','1924','Çırağan Cadddesi no:30 ',130,1234567812)''')

c=isaretci.execute(''' INSERT INTO veli_bilgileri(ogrenci_no,ad,iş) VALUES 
(1020,'ŞEYMA ATEŞ','ÖĞRETMEN')''')

e=isaretci.execute(''' INSERT INTO dersler(ders_id,adi,kredi) VALUES 
(314159,'Bilgisayar Bilimi',4)''')

baglanti.commit()
#bilgilerin kaydedilmesi için yazılması gerekiyor yoksa kaydetmez.
