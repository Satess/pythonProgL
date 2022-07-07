import pygame, sys, PIL  # kütüphane çağırma işlemi
from PIL import Image
genislik=800
yukseklik=600

pygame.init()  # python fonksiyonlarının kullanılabilmesi için yazılması gereken bir kod
# oyun için bir pencere oluşturulacak ilk olarak boyutunu bir değişken ile belirleyelim.
boyut = (genislik, yukseklik)

# penceremizi oluşturalım
pencere = pygame.display.set_mode(
    boyut)  # penceremizi oluşturduk ve boyut değişkenini pencere değişkenimiz ile eşledik.

top = pygame.image.load("/Users/sates/Desktop/top.jpg")
x = 0
y = 0

pygame.mixer.music.load("/Users/sates/Desktop/52.1.wav")  # müzik ekleme
# müzik çalması için yazdığımız kod


saat = pygame.time.Clock()  # fps yani saniyedeki piksel sayısını belirlemek için bir değişken oluşturduk.
# while döngüsü içerisinde de bu değişkenin saniyede kaç piksel ilerleyeceğini yazacağızç
# bunu yapma sebebimiz her bilgisayarda saniyedeki piksel sayısının farklı olmasıdır.
pygame.mouse.set_visible(0)

sprite_Grup=pygame.sprite.Group()

class Parca(pygame.sprite.Sprite):
    def __init__(self,x=genislik/2, y=yukseklik/2): # python fonksiyonlarını kullanmak için init() aktifleştirmiştik burda da nesne tab. kullanabilmek için aktifleştiriyoruz.
    #burda eğer x ve y değerine değer girilmez ise ortasını alacak girilirse sıkıntı yok değer girilebilir artık
        super().__init__() #sprite sınıfından miras aldığımız için onun da özelliklerini çağırıyoruz bu işlemi de super fonk. yapıyoruz.
#parçacıkların bir resme ve boyuta ihtiyacı var yani image ve rect boyutları olması gerekiyor.
        self.image=top #oluşturuduğumuz nesneye genişlik ve yükseklik verdik yani boyutlandırdık
        #self.image.fill((255,0,0)) #oluşturduğumuz nesneyi fill komutu yardımı ile bir renk ile doldurduk.
        self.rect=self.image.get_rect()
#parçacığın koor. belirlenmesi gerekiyor ve istenilen yerden belirlenebilir mesela orta ya da sol üst gibi
        self.rect.center=(x,y)
    def Parcacikhareketettir(self):
        self.rect.x+=5
        if self.rect.x>genislik:
            self.rect.x=0



parca1 =Parca() #bu şekilde Parca sınıfından bir parca1 nesnesi türetildi
parca2=Parca(50,50)
sprite_Grup.add(parca1,parca2) #daha önce oluşturduğumuz sprite grubuna parça1'i ekledik
#oluşturduğumuz sprite'ı ekranda göstermemiz gerekiyor!
#parca1 ve parca2 aynı koor. olduğundan üst üste binecek bu yüzden sınıf tanımlarken self kısmında koor belirtilmeli

while True:  # bu döngü sayesinde pencereyi açık tutuyoruz.
    saat.tick(60)  # saniyede 60 kare değişecek yani 60 piksel ilerleyecek.
    for event in pygame.event.get():  # pygame eventlerden yani olaylardan oluşur.
        if event.type == pygame.QUIT: sys.exit()  # burda eğer birisi x tuşuna bastıysa sayfayı kapat diyoruz.

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if top.get_size()[0] + x < 800:
                    x += 10
            if event.key == pygame.K_LEFT:
                if x > 0:
                    x -= 10
            if event.key == pygame.K_UP:
                if y > 0:
                    y -= 10
            if event.key == pygame.K_DOWN:
                if top.get_size()[1] + y < 600:
                    y += 10  # yenin değerini artırınca aşağıya iniyor
    parca1.Parcacikhareketettir()
    parca2.Parcacikhareketettir()

    pencere.fill((255, 255,255))  # yazı hareket ettiğinde arka planı etkilemesin sadece yazı hareket ediyormuş gibi olsun diye yazıyoruz

    sprite_Grup.draw(pencere)
    pencere.blit(top, (x, y))

    pygame.display.update()