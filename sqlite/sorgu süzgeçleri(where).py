import sqlite3

baglanti= sqlite3.connect('/Users/sates/Desktop/okul.db')
isaretci=baglanti.cursor()

db=isaretci.execute('SELECT adi FROM ogrenciler WHERE cinsiyeti="K"')
print(db.fetchall())

baglanti.commit()