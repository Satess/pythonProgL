import pygame,sys,PIL #kütüphane çağırma işlemi
from PIL import Image
import time
pygame.init() #python fonksiyonlarının kullanılabilmesi için yazılması gereken bir kod
#oyun için bir pencere oluşturulacak ilk olarak boyutunu bir değişken ile belirleyelim.
boyut=(800,600)

#penceremizi oluşturalım
pencere=pygame.display.set_mode(boyut) #penceremizi oluşturduk ve boyut değişkenini pencere değişkenimiz ile eşledik.
pygame.mixer.music.load("/Users/sates/Desktop/52.1.wav") #müzik ekleme
pygame.mixer.music.play() #müzik çalması için yazdığımız kod
pygame.mixer.music.set_volume(0.2) #müziğin ses şiddetini ayarlama
time.sleep(6)
pygame.mixer.music.stop() #müziği durdurma

pygame.mouse.set_visible(0) #mouse 'u ekranda göstermemek için yazılan kod

saat=pygame.time.Clock() # fps yani saniyedeki piksel sayısını belirlemek için bir değişken oluşturduk.
#while döngüsü içerisinde de bu değişkenin saniyede kaç piksel ilerleyeceğini yazacağızç
#bunu yapma sebebimiz her bilgisayarda saniyedeki piksel sayısının farklı olmasıdır.

while True: #bu döngü sayesinde pencereyi açık tutuyoruz.
    saat.tick(60) #saniyede 60 kare değişecek yani 60 piksel ilerleyecek.
    for event in pygame.event.get(): #pygame eventlerden yani olaylardan oluşur.
        if event.type==pygame.QUIT:sys.exit() #burda eğer birisi x tuşuna bastıysa sayfayı kapat diyoruz.

    pencere.fill((255,255,255)) # yazı hareket ettiğinde arka planı etkilemesin sadece yazı hareket ediyormuş gibi olsun diye yazıyoruz

    sol, orta, sag=pygame.mouse.get_pressed() #mouse ile müziği kontrol ettirme işlemi

    if sol==1: #eğer sol tuşa basılmış ise
        pygame.mixer.music.unpause() #müziği başlat
    if sag==1:
        pygame.mixer.music.pause() #müziği durdur
    pygame.display.update()