import pygame,sys #kütüphane çağırma işlemi
pygame.init() #python fonksiyonlarının kullanılabilmesi için yazılması gereken bir kod
#oyun için bir pencere oluşturulacak ilk olarak boyutunu bir değişken ile belirleyelim.
boyut=(800,600)
#penceremizi oluşturalım
pencere=pygame.display.set_mode(boyut) #penceremizi oluşturduk ve boyut değişkenini pencere değişkenimiz ile eşledik.
font=pygame.font.SysFont("Helvetica",100)#yazı yazdırmak için font ayarlarını yapıyorum.
satesgame=font.render("SATES GAME",1,(255,255,255),(0,0,0))

x=0
y=0

saat=pygame.time.Clock() # fps yani saniyedeki piksel sayısını belirlemek için bir değişken oluşturduk.
#while döngüsü içerisinde de bu değişkenin saniyede kaç piksel ilerleyeceğini yazacağız.
#bunu yapma sebebimiz her bilgisayarda saniyedeki piksel sayısının farklı olmasıdır.

while True: #bu döngü sayesinde pencereyi açık tutuyoruz.
    saat.tick(60) #saniyede 60 kare değişecek yani 60 piksel ilerleyecek.
    for event in pygame.event.get(): #pygame eventlerden yani olaylardan oluşur.
        if event.type==pygame.QUIT:sys.exit() #burda eğer birisi x tuşuna bastıysa sayfayı kapat diyoruz.

    #pencere.fill((0,0,0)) # yazı hareket ettiğinde arka planı etkilemesin
    # sadece yazı hareket ediyormuş gibi olsun diye yazıyoruz
    #bu kodumuzda dikkat edilmesi gereken şey;
    # fill içine yazılan renk ile arka plan renginin rgb kodlarının aynı olması gerektiği
    x+=1 #yazıyı soldan sağa bir piksel ilerletir.
    pencere.blit(satesgame, (x,y)) #yazımızı ekranda göstermek için yazdığımız bir kod
    pygame.display.update()

