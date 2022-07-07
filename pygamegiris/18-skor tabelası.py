import pygame, sys, os ,random # kütüphane çağırma işlemi

genislik = 800
yukseklik = 600

pygame.init()
boyut = (genislik, yukseklik)
pencere = pygame.display.set_mode(boyut)

x = 0
y = 0

pikselsayisi = pygame.time.Clock()

oyun_dosyasi = os.path.dirname(__file__)
resim_dosyasi = os.path.join(oyun_dosyasi, "image/oyun_resimleri")

class Parca(pygame.sprite.Sprite):
    def __init__(self, x=genislik / 2, y=yukseklik / 2):
        super().__init__()
        self.image = pygame.Surface((30,50))
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()
        self.rect.x=0
        self.rect.y=y

    def update(self, *args):
        up, down, right, left = args
        if self.rect.y + self.rect.size[1] > yukseklik:
            self.rect.y = yukseklik-self.rect.size[1]
        if self.rect.y < 0:
            self.rect.y = 0

        if up:
            self.rect.y -= 10
        if down:
            self.rect.y += 10

class Mermi(pygame.sprite.Sprite):
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

        if self.rect.right<0:
            self.rect.y = random.randrange(yukseklik - self.rect.height)
            self.rect.x = random.randrange(genislik + 40, genislik + 100)
            self.speedx = random.randrange(1, 12)

sprite_Grup = pygame.sprite.Group()

for i in range(8):
    mermi=Mermi()
    sprite_Grup.add(mermi)

parca1 = Parca()  # bu şekilde Parca sınıfından bir parca1 nesnesi türetildi
#parca2 = Parca(50, 50)
sprite_Grup.add(parca1)  # daha önce oluşturduğumuz sprite grubuna parça1'i ekledik
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
