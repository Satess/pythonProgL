import pygame, sys, os ,random # kütüphane çağırma işlemi
# pygame oyun kütüphanesi
#sys ve os dosya işlemleri için eklediğimiz kütüphaneler
#random parçaçıkları eklemek için kullanacağız bu sebeple ekliyoruz.

genislik = 800 #sahne genişliği için değişken oluşturup değer verdik.
yukseklik = 600 #sahne yüksekliği için değişken oluşturup değer verdik.

pygame.init() # python fonksiyonlarını yazabilmek için kullandığımız komut
boyut = (genislik, yukseklik) #sahnemizin genişlik ve yükseklik değerlerini bir tuple içerisine atıyoruz.
pencere = pygame.display.set_mode(boyut) #sahne oluşturma komutu

x = 0 #karakterimizin x düzlemindeki konumu için değişken oluşturuyoruz.
y = 0 #karakterimizin y düzlemindeki konumu için değişken oluşturuyoruz.
pikselsayisi = pygame.time.Clock() #saniyede aktarılan piksel sayısını belirlemek için yazdığımız kod.

#oyun_dosyasi = os.path.dirname(__file__) #projenin dosyalarına ulşamak için yazdığımız komut
#resim_dosyasi = os.path.join(oyun_dosyasi, "image/oyun_resimleri") #oyun resimlerine ulaşmak için yazdığımız komut

class Karakter(pygame.sprite.Sprite): #hareketli cisimleri eklemek için sınıf oluşturuyoruz.
    def __init__(self, x=genislik / 2, y=yukseklik / 2): #sınıfın özelliklerini ekliyoruz.
        super().__init__() #Sprite sınıfından miras aldığımız için super fonk ile Sprite sınıfının özelliklerini de
        #yeni sınıfımıza aktarız.
        self.image = pygame.Surface((30,50)) # karakter olarak surface oluşturuyoruz. (Bir kutu)
        self.image.fill((0,255,255)) #oluşturduğumuz kutunun içini renk ile dolduruyoruz.
        self.rect = self.image.get_rect()  #konumlandırıyoruz
        self.rect.x=0 #cismimiz c düzleminde hep x=0 olacağı için sıfır değerini verdik
        self.rect.y=y # cismimiz y düzleminde hareket edece ve y konumunu verdik

    def update(self, *args): #karakterin hareketlerini ekliyoruz.
        up, down, right, left = args #tuple olarak args bölümüne ekledik
        if self.rect.y + self.rect.size[1] > yukseklik: # eğer cismin konumu sahne yüksekliğini geçer ise:
            self.rect.y = yukseklik-self.rect.size[1] # sahne yüksekliğinden cismin bitiş değerini çıkar
            #yani cismi sahneni başına taşı
        if self.rect.y < 0: #cismin konumu - değerlere gider ise :
            self.rect.y = 0 #cimsi sıfır noktasına taşı

        if up:
            self.rect.y -= 10 # hareket birimi
        if down:
            self.rect.y += 10  # hareket birimi

class RandomParcalar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((20,20))
        self.image.fill((240,100,30))
        self.rect=self.image.get_rect()
        self.rect.y=random.randrange(yukseklik-self.rect.height)
        self.rect.x=random.randrange(genislik+40,genislik+100)
        self.speedx=random.randrange(1,12)

    def update(self,*args):
        self.rect.x-=self.speedx

        if self.rect.right<0: #parcacık tamamen ekrandan çıktığında :
            #yeniden aynı şekilde oluşsun (yukardaki kodun aynısı)
            self.rect.y = random.randrange(yukseklik - self.rect.height)
            self.rect.x = random.randrange(genislik + 40, genislik + 100)
            self.speedx = random.randrange(1, 12)

sprite_Grup = pygame.sprite.Group()

for i in range(8):
    parca=RandomParcalar()
    sprite_Grup.add(parca)

karakter1 = Karakter()  # bu şekilde Parca sınıfından bir parca1 nesnesi türetildi
#parca2 = Parca(50, 50)
sprite_Grup.add(karakter1)  # daha önce oluşturduğumuz sprite grubuna parça1'i ekledik
# oluşturduğumuz sprite'ı ekranda göstermemiz gerekiyor!
# parca1 ve parca2 aynı koor. olduğundan üst üste binecek bu yüzden sınıf tanımlarken self kısmında koor belirtilmeli

while True:  # bu döngü sayesinde pencereyi açık tutuyoruz.
    # hangi tuşa basılıyor ya da herhangi bir tuşa basılıyor mu görmek için fonksiyon yazıyoruz.
    tuslar = pygame.key.get_pressed()
    pikselsayisi.tick(60)  # saniyede 60 kare değişecek yani 60 piksel ilerleyecek.

    for event in pygame.event.get():  # pygame eventlerden yani olaylardan oluşur.
        if event.type == pygame.QUIT: sys.exit()  # burda eğer birisi x tuşuna bastıysa sayfayı kapat diyoruz.

    up, down, right, left = tuslar[pygame.K_UP], tuslar[pygame.K_DOWN], tuslar[pygame.K_RIGHT], tuslar[pygame.K_LEFT]
    sprite_Grup.update(up, down, right, left)

    pencere.fill((255, 255,255))  # yazı hareket ettiğinde arka planı etkilemesin sadece yazı hareket ediyormuş gibi olsun diye yazıyoruz

    sprite_Grup.draw(pencere)

    pygame.display.update()
