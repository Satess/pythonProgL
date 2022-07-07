import sqlite3

baglanti= sqlite3.connect('/Users/sates/Desktop/okul.db')
isaretci=baglanti.cursor()

#db=isaretci.execute('SELECT * FROM ogrenciler')
#db2=isaretci.execute('SELECT adi FROM ogretmenler')
#db3=isaretci.execute('SELECT kurulus_tarihi FROM okul_bilgileri')
#db4=isaretci.execute('SELECT iş FROM veli_bilgileri')
db5=isaretci.execute('SELECT adi FROM dersler')
#sqlite veri alma işlemi SELECT ifadesi ile yapılır.
#* sayesinde bütün alanları seçiyoruz.

#satırları teker teker çağırmak için:
'''a=1
while a<4:
    print(db5.fetchone())
    a+=1'''

#tüm veriyi almak için:
#print(db5.fetchall())

#işaretçinin okuduğu sorgu sonucunda istediğimiz kadar satır yakalamak için:
print(db5.fetchmany(2))


baglanti.commit()