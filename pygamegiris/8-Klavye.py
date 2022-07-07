import pygame,sys,PIL #kütüphane çağırma işlemi
from PIL import Image



pygame.init() #python fonksiyonlarının kullanılabilmesi için yazılması gereken bir kod
#oyun için bir pencere oluşturulacak ilk olarak boyutunu bir değişken ile belirleyelim.
boyut=(800,600)


#penceremizi oluşturalım
pencere=pygame.display.set_mode(boyut) #penceremizi oluşturduk ve boyut değişkenini pencere değişkenimiz ile eşledik.


top=pygame.image.load("/Users/sates/Desktop/top.jpg")
x=0
y=0

#pygame.mixer.music.load("/Users/sates/Desktop/52.1.wav") #müzik ekleme
 #müzik çalması için yazdığımız kod



saat=pygame.time.Clock() # fps yani saniyedeki piksel sayısını belirlemek için bir değişken oluşturduk.
#while döngüsü içerisinde de bu değişkenin saniyede kaç piksel ilerleyeceğini yazacağızç
#bunu yapma sebebimiz her bilgisayarda saniyedeki piksel sayısının farklı olmasıdır.
pygame.mouse.set_visible(0)

while True: #bu döngü sayesinde pencereyi açık tutuyoruz.
    saat.tick(60) #saniyede 60 kare değişecek yani 60 piksel ilerleyecek.
    for event in pygame.event.get(): #pygame eventlerden yani olaylardan oluşur.
        if event.type==pygame.QUIT:sys.exit() #burda eğer birisi x tuşuna bastıysa sayfayı kapat diyoruz.

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                if top.get_size()[0]+x<800:
                    x+=10
            if event.key==pygame.K_LEFT:
                if x>0:
                    x-=10
            if event.key==pygame.K_UP:
                if  y > 0:
                    y-=10
            if event.key==pygame.K_DOWN:
                if top.get_size()[1] + y < 600:
                    y+=10#yenin değerini artırınca aşağıya iniyor

    pencere.fill((255,255,255)) # yazı hareket ettiğinde arka planı etkilemesin sadece yazı hareket ediyormuş gibi olsun diye yazıyoruz

    pencere.blit(top,(x,y))
    


    pygame.display.update()