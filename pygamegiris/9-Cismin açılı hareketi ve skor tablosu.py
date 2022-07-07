import pygame, sys, os, random

genislik=800
yukseklik=600

pygame.init()

boyut=(genislik,yukseklik)

sahne=pygame.display.set_mode(boyut)

pikselsayisi=pygame.time.Clock()


x=0
y=0
score=0 #skorun artmasını sağlayabilmek için değişken oluşturduk

pygame.mixer.music.load("/Users/sates/Desktop/1606.wav")
font=pygame.font.SysFont("Helvetica",50) #skor için bir metin oluşturduk.


class Karakter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((30,50))
        self.image.fill((45,60,98))
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=y

    def update(self, *args):
        up, down, right, left=args
        if self.rect.y+self.rect.size[1]>yukseklik:
            self.rect.y=yukseklik-self.rect.size[1]
        if self.rect.y<0:
            self.rect.y=0

        if up:
            self.rect.y-=10
        if down:
            self.rect.y+=10

class Randomcisim(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((20,20))
        self.image.fill((12,40,250))
        self.rect=self.image.get_rect()
        self.rect.y=random.randrange(yukseklik-self.rect.height)
        self.rect.x=random.randrange(genislik+40,genislik+100)
        self.speedx=random.randrange(5,13) #x y değerine göre yavaş kalmasın diye hızını değiştirdik
        self.speedy=random.randrange(-2,2) #açılı hareket etsin istediğimizden hem x hem y hızı ekliyoruz.

    def update(self, *args):
        self.rect.x-=self.speedx
        self.rect.y+=self.speedy


        if self.rect.right<0:
            self.rect.y = random.randrange(yukseklik - self.rect.height)
            self.rect.x = random.randrange(genislik + 40, genislik + 100)
            self.speedx = random.randrange(5, 13)
            self.speedy=random.randrange(-2,2) #ekrandan çıktığında y değeri için de yeniden dönsün diye yazdık
            global score #score değişkeni global olduğu için belirttik.
            score+=1 #score değişkeni cisim karaktere çarpmadan sahneden çıktığında olduğu için bu bölümde yazıldı

sprite_Grup=pygame.sprite.Group()

karakter1=Karakter()
sprite_Grup.add(karakter1)
cisimler=pygame.sprite.Group() #cisimler diye yeni bir sprite grubu oluşturduk

for i in range(8):
    cisim=Randomcisim()
    sprite_Grup.add(cisim)
    cisimler.add(cisim) # bu kod ile hem cisim hem de sprite grup içerisine cisim nesnesini eklemiş olduk


while True:

    tuslar=pygame.key.get_pressed()

    pikselsayisi.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()

    up, down, right, left =tuslar[pygame.K_UP],tuslar[pygame.K_DOWN],tuslar[pygame.K_RIGHT],tuslar[pygame.K_LEFT]


    sprite_Grup.update(up,down, right, left)

    SkorFont=font.render("Skor : {}".format(score), 1, (0, 0, 0)) #skor değişkeninin yazılma şeklini belirledik

    sahne.fill((255,255,255))
    sprite_Grup.draw(sahne)
    #bu işlemi fill özelliğinden sonra yapmalıyız çünkü fill sürekli ekranı beyaz renk ile doldurduğundan yazımız görünmüyor.
    sahne.blit(SkorFont, ((genislik - SkorFont.get_size()[0]), (yukseklik - SkorFont.get_size()[1]))) #değişkeni ekrana yazdırdık.

    durum=pygame.sprite.spritecollide(karakter1,cisimler,False)
    if durum:
        pygame.mixer.music.play()
        sahne.fill((0,0,0))
        sahne.blit(pygame.font.SysFont("Helvetica",100).render(" GAME OVER",1,(255,0,0)),(150,250))
        pygame.display.update()
        pygame.time.wait(5000)
        sys.exit()

    pygame.display.update()