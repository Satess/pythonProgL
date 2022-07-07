import pygame,sys,PIL #kütüphane çağırma işlemi
from PIL import Image
pygame.init() #python fonksiyonlarının kullanılabilmesi için yazılması gereken bir kod
#oyun için bir pencere oluşturulacak ilk olarak boyutunu bir değişken ile belirleyelim.
boyut=(800,600)

#penceremizi oluşturalım
pencere=pygame.display.set_mode(boyut) #penceremizi oluşturduk ve boyut değişkenini pencere değişkenimiz ile eşledik.

pygame.mixer.music.load("/Users/sates/Desktop/52.1.wav") #müzik ekleme
 #müzik çalması için yazdığımız kod


pygame.mouse.set_visible(0) #mouse 'u ekranda göstermemek için yazılan kod

pygame.mouse.get_rel() #mouse hareket miktarı

pygame.mouse.get_focused() #mouse oyun ekranı içerisinde mi? bunu kontrol eder.

pygame.mouse.set_pos(100,100) #oyun başladığında mosue'un bulunduğu yeri bu şekilde belirleyebiliriz yada herhangi bir koşulda

pygame.mouse.get_pressed() #3 tuple değeri alan sol,orta, sağ bir fonksiyon mouse üzerinde hangi tuşa basıldı gösterir ve buna göre işlem yapar.

pygame.mouse.set_visible(0) #bu değer True olduğunda mouse ekranda görünür False olursa görünmez.

saat=pygame.time.Clock() # fps yani saniyedeki piksel sayısını belirlemek için bir değişken oluşturduk.
#while döngüsü içerisinde de bu değişkenin saniyede kaç piksel ilerleyeceğini yazacağızç
#bunu yapma sebebimiz her bilgisayarda saniyedeki piksel sayısının farklı olmasıdır.

while True: #bu döngü sayesinde pencereyi açık tutuyoruz.
    saat.tick(60) #saniyede 60 kare değişecek yani 60 piksel ilerleyecek.
    for event in pygame.event.get(): #pygame eventlerden yani olaylardan oluşur.
        if event.type==pygame.QUIT:sys.exit() #burda eğer birisi x tuşuna bastıysa sayfayı kapat diyoruz.

    pencere.fill((255,255,255)) # yazı hareket ettiğinde arka planı etkilemesin sadece yazı hareket ediyormuş gibi olsun diye yazıyoruz

    xHareket,yHareket=pygame.mouse.get_rel()

    if xHareket>100 or xHareket<-100 or yHareket>100 or yHareket<-100:
        pygame.mixer.music.play()


    pygame.display.update()