import pygame, sys, os, random

genislik=800
yukseklik=600

pygame.init()

boyut=(genislik,yukseklik)

sahne=pygame.display.set_mode(boyut)

pikselsayisi=pygame.time.Clock()

x=0
y=0

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
        self.speedx=random.randrange(1,12)

    def update(self, *args):
        self.rect.x-=self.speedx

        if self.rect.right<0:
            self.rect.y = random.randrange(yukseklik - self.rect.height)
            self.rect.x = random.randrange(genislik + 40, genislik + 100)
            self.speedx = random.randrange(1, 12)

sprite_Grup=pygame.sprite.Group()

karakter1=Karakter()
sprite_Grup.add(karakter1)

for i in range(15):
    cisim=Randomcisim()
    sprite_Grup.add(cisim)


while True:

    tuslar=pygame.key.get_pressed()

    pikselsayisi.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()

    up, down, right, left =tuslar[pygame.K_UP],tuslar[pygame.K_DOWN],tuslar[pygame.K_RIGHT],tuslar[pygame.K_LEFT]


    sprite_Grup.update(up,down, right, left)

    sahne.fill((255,255,255))

    sprite_Grup.draw(sahne)

    pygame.display.update()