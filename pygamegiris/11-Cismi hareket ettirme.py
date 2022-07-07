#1-Kütüphane ve Modül aktifleştirme işlemi

import pygame, sys, os
pygame.init()

#2-Sahne İşlemleri

genislik=800
yukseklik=600

boyut=(genislik,yukseklik)

sahne=pygame.display.set_mode(boyut)

pikselSayisi=pygame.time.Clock()

#5-Oyun içerisine eklenecek resim dosyasının dosya konumun tanıtılması
oyun_dosyasi=os.path.dirname(__file__)
resim_dosyasi=os.path.join(oyun_dosyasi,"image/oyun_resimleri")


#3-Cisim hareketleri için değişken oluşturma

x=0 #cismin hareket etmesi için kullanılan x koor. değişkeni
y=0 #cismin hareket etmesi için kullanılan y koor. değişkeni

sprite_Grup=pygame.sprite.Group()

class Karakter(pygame.sprite.Sprite):
    def __init__(self,x=genislik/2 , y=yukseklik/2): #x ve y değerlerine cisim her seferinde sahnenin ortasında olsun diye
        #genislik/2 ve yukseklik/2 değeri atandı.
        super().__init__() #miras alınan sınıfın özelliklerini yeni sınıfa ekler
        self.image=pygame.image.load(os.path.join(resim_dosyasi,"canavar3.png")).convert()
        #convert resmin daha iyi görünmesini sağlayan bir komut - eklenmese de olabilir kodda hata vermez.
        self.image.set_colorkey((0,0,0)) #convert eklendiğinde resim arkaplanına siyah renk ataması yapar.
        #arkaplandaki siyah rengi engellemek için yazılan siyah renk engelle kodu.
        self.rect=self.image.get_rect() #karakterin boyutlandırma işlemi
        self.rect.center=(x,y) #karakterin konum işlemi

    def update(self,*args):
        up, down, right, left=args

        if self.rect.x>genislik:
            self.rect.x=0
        if self.rect.x<0:
            self.rect.x=genislik
        if self.rect.y>yukseklik:
            self.rect.y=0
        if self.rect.y<0:
            self.rect.y=yukseklik
        if right:
            self.rect.x+=10
        if left:
            self.rect.x-=10
        if up:
            self.rect.y-=10
        if down:
            self.rect.y+=10

karakter1=Karakter() #karakter sınıfından karakter1 adında bir karakter oluşturduk.

sprite_Grup.add(karakter1) #karakteri sprite grubuna ekledik



#4-Sürekli gerçekleşecek işlemler için kullanılan bölüm

while True:
    tuslar=pygame.key.get_pressed() # hangi tuşa basılmış ve o tuş hangi işlemi gerçekleştiriyor.
    pikselSayisi.tick(60)

    #Bir exit bölümünden sahneyi kapatana kadar oyunun açık kalmasını sağlayan kodumuz.
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()


    if tuslar[pygame.K_UP] or tuslar[pygame.K_DOWN] or tuslar[pygame.K_LEFT] or tuslar[pygame.K_RIGHT]:
        up, down, right, left = tuslar[pygame.K_UP],tuslar[pygame.K_DOWN],tuslar[pygame.K_RIGHT],tuslar[pygame.K_LEFT]

        sprite_Grup.update(up,down,right,left)

    sahne.fill((255,255,255)) #cisim hareketlerinde sahnenin bozulmaması fill komutu ile renk eklemesi yapılır.

    sprite_Grup.draw(sahne) #karakterin sahnede görünmesini sağlar.

    pygame.display.update() #sahnenin kendini sürekli güncellemesi için

