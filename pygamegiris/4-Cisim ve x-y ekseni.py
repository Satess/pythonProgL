import pygame,sys,PIL #kütüphane çağırma işlemi
from PIL import Image
pygame.init() #python fonksiyonlarının kullanılabilmesi için yazılması gereken bir kod
#oyun için bir pencere oluşturulacak ilk olarak boyutunu bir değişken ile belirleyelim.
boyut=(800,600)

#penceremizi oluşturalım
pencere=pygame.display.set_mode(boyut) #penceremizi oluşturduk ve boyut değişkenini pencere değişkenimiz ile eşledik.

top=pygame.image.load("/Users/sates/Desktop/tts.jpg")

topX=top.get_size()[0] #topun x düzlemindeki büyüklüğünü hesaplıyor
topY=top.get_size()[1] #topun y düzlemindeki büyüklüğünü hesaplıyor
x=0
y=0
xYON=1 #yazının yönü için işlem yapılacak bu sebep ile bir değişken oluşturduk
yYON=1

saat=pygame.time.Clock() # fps yani saniyedeki piksel sayısını belirlemek için bir değişken oluşturduk.
#while döngüsü içerisinde de bu değişkenin saniyede kaç piksel ilerleyeceğini yazacağızç
#bunu yapma sebebimiz her bilgisayarda saniyedeki piksel sayısının farklı olmasıdır.

while True: #bu döngü sayesinde pencereyi açık tutuyoruz.
    saat.tick(60) #saniyede 60 kare değişecek yani 60 piksel ilerleyecek.
    for event in pygame.event.get(): #pygame eventlerden yani olaylardan oluşur.
        if event.type==pygame.QUIT:sys.exit() #burda eğer birisi x tuşuna bastıysa sayfayı kapat diyoruz.

    pencere.fill((255,255,255)) # yazı hareket ettiğinde arka planı etkilemesin
    # sadece yazı hareket ediyormuş gibi olsun diye yazıyoruz
    #bu kodumuzda dikkat edilmesi gereken şey
    # fill içine yazılan renk ile arka plan renginin rgb kodlarının aynı olması gerektiği
    if x>800-topX or x<0: #yazının sınırlardan sekmesi için yazılıyor
        xYON*=-1
    if y>600-topY or y<0:
        yYON*=-1

    x+=4* xYON #yazıyı soldan sağa bir piksel ilerletir.
    y+=4* yYON
    pencere.blit(top, (x, y))
    pygame.display.update()

