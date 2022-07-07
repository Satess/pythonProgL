
import sqlite3

#Bir sql dosyasını metin dosyası ile açamayız!!!

baglanti=sqlite3.connect('/Users/sates/Desktop/balhza.db')

#veritabanı ile bağlantı kurduğumuzda işlem yapabilmemiz için nesnenin oluşturulması gerekir.
#işaretçi nesnesi bağlantı nesnesinin cursor() özelliği ile oluşturulur.

isaretci=baglanti.cursor()

#patikada dosya yok ise dosyayı oluşturur ve
# bağlantıyı kurar eğer dosya var ise sadece bağlantı kurar.

baglanti.commit() #kaydetme işlemi yapar.



