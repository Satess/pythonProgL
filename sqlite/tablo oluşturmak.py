
import sqlite3

baglanti=sqlite3.connect('/Users/sates/Desktop/hza.db')
isaretci=baglanti.cursor()


isaretci.execute('''CREATE TABLE ogrenciler(kayit_no INTEGER PRIMARY KEY,
ogrenci_no INTEGER NOT NULL,
adi VARCHAR(50),
soyadi VARCHAR (50),
cinsiyeti VARCHAR (1),
sinif VARCHAR (50),
telefon_numarasi VARCHAR (12),
velisi VARCHAR (75),
dogum_yeri VARCHAR(25))''')


isaretci.execute(''' CREATE TABLE ogretmenler(kayit_no INTEGER PRIMARY KEY,
adi VARCHAR(40),
soyadi VARCHAR(40),
brans VARCHAR(20),
telefon_no VARCHAR(20),
hizmet_puanı INTEGER)''')

isaretci.execute(''' CREATE TABLE okul_bilgileri (id INTEGER PRIMARY KEY, 
ad VARCHAR(100),
kurulus_tarihi VARCHAR(20),
adres VARCHAR(100),
kontenjan INTEGER,
telefon VARCHAR(11))''')

isaretci.execute('''CREATE TABLE veli_bilgileri(ogrenci_no INTEGER PRIMARY KEY, 
ad VARCHAR(50),
iş VARCHAR(20),
adres VARCHAR(100),
yas INTEGER)''')

isaretci.execute(''' CREATE TABLE dersler(ders_id INTEGER PRİMARY KEY, 
adi VARCHAR(100),
kredi INTEGER)''')



baglanti.commit() #kaydetme işlemi



#databasede değişmeyen tek bilgi birincil(ana) anahtarımız PRİMARY KEY'dir.

#otomatik olarak artıyor ise girmeye gerek yok otomatik olarak atanır.

#veri tabanına girilecek verinin ne türde olduğu önceden belirlenir.

#string tarzında veri girildiğinde veri uzunluğu verilir.

#her alana tek tür veri girilir.

#cinsiyet gibi veriler tek boyutludur------ E/K gibi

#kısa metinler girileceği zaman en fazla 500 karakter girilebilir

#bu tür alanlara sqlde değişken karakter diyoruz.

#daha uzun metinler içi text veri tipi kullanılabilir.

#BU İŞLEVİ ÇALIŞTIRABİLMEMİZ İÇİN isaretci.execute('''....''') şeklinde yazmamız gerekir.


