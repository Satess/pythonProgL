import sqlite3

baglanti= sqlite3.connect('/Users/sates/Desktop/1.db')
isaretci=baglanti.cursor()

db=isaretci.execute('SELECT adi,soyadi,telefon_numarasi FROM ogrenciler')
for i in db.fetchmany(1):
    print(i['adi'],i['soyadi'],i['telefon_numarasi'])

