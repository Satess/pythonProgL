#veriler INSERT INTO  komutu ile girilir.

import sqlite3

baglanti= sqlite3.connect('/Users/sates/Desktop/6.db')
isaretci=baglanti.cursor()


isaretci.execute('''CREATE TABLE ogretmenler(ogr_no INTEGER PRIMARY KEY,
adi VARCHAR(50),
soyadi VARCHAR (50),
sinif VARCHAR (3))''')

#a=isaretci.execute('''INSERT INTO ogretmenler(ogr_no,adi,soyadi,sinif) VALUES (22,'Şeyma','Ateş','1')''')
#b=isaretci.execute('''INSERT INTO ogretmenler(ogr_no,adi,soyadi,sinif) VALUES (23,'Derya','Çakır','2')''')
#c=isaretci.execute('''INSERT INTO ogretmenler(ogr_no,adi,soyadi,sinif) VALUES (24,'Burak','Yılmaz','3')''')
adi=input("Öğretmenin Adi: ")
soyadi=input("Öğretmen Soyadı: ")

#önce hangi sınıflar var onları bulalım ve bir sözlük hazırlayalım

db=isaretci.execute('SELECT sinif FROM ogretmenler')
siniflar={}
c=1
for i in db.fetchall():
    if not i[0] in siniflar:
        siniflar[c]=i[0]
        c+=1
print("Hangi şubenin sınıf öğretmenidir?")
for i in siniflar:
    print(i,':',siniflar[i])

sinif=input('Seçiminiz: ')

isaretci.execute('INSERT INTO ogretmenler (adi,soyadi,sinif) VALUES ("%s","%s","%s")' % (adi,soyadi,siniflar[int(sinif)]))


baglanti.commit() #bilgilerin kaydedilmesi için yazılması gerekiyor yoksa kaydetmez.
baglanti.close()
