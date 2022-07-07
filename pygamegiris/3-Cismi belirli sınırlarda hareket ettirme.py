import pygame,sys #kütüphane çağırma işlemi
pygame.init() #python fonksiyonlarının kullanılabilmesi için yazılması gereken bir kod
#oyun için bir pencere oluşturulacak ilk olarak boyutunu bir değişken ile belirleyelim.
boyut=(800,600)

#penceremizi oluşturalım
pencere=pygame.display.set_mode(boyut) #penceremizi oluşturduk ve boyut değişkenini pencere değişkenimiz ile eşledik
font=pygame.font.SysFont("Helvetica",100)#yazı yazdırmak için font ayarlarını yapıyorum.
satesgame=font.render("SATES GAME",1,(255,255,255),(0,0,0))
yaziboyutX=satesgame.get_size()[0]

#print(yaziboyut) yazı boyunu öğrenmek için yazdık
x=0
y=0
xYON=1 #yazının yönü için işlem yapılacak bu sebep ile bir değişken oluşturduk
saat=pygame.time.Clock() # fps yani saniyedeki piksel sayısını belirlemek için bir değişken oluşturduk.
#while döngüsü içerisinde de bu değişkenin saniyede kaç piksel ilerleyeceğini yazacağızç
#bunu yapma sebebimiz her bilgisayarda saniyedeki piksel sayısının farklı olmasıdır.
while True: #bu döngü sayesinde pencereyi açık tutuyoruz.
    saat.tick(60) #saniyede 60 kare değişecek yani 60 piksel ilerleyecek.
    for event in pygame.event.get(): #pygame eventlerden yani olaylardan oluşur.
        if event.type==pygame.QUIT:sys.exit() #burda eğer birisi x tuşuna bastıysa sayfayı kapat diyoruz.

    if x>800-yaziboyutX or x<0: #yazının sınırlardan sekmesi için yazılıyor
        xYON*=-1

    x+=1* xYON #yazıyı soldan sağa bir piksel ilerletir.
    pencere.blit(satesgame, (x,y)) #yazımızı ekranda göstermek için yazdığımız bir kod
    pygame.display.update()

