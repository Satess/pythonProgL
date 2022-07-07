import pygame,sys #kütüphane çağırma işlemi

pygame.init() #python fonksiyonlarının kullanılabilmesi için yazılması gereken bir kod
#oyun için bir pencere oluşturulacak ilk olarak boyutunu bir değişken ile belirleyelim.

boyut=(800,600)

#penceremizi oluşturalım
pencere=pygame.display.set_mode(boyut) #penceremizi oluşturduk ve boyut değişkenini pencere değişkenimiz ile eşledik.

font=pygame.font.SysFont("Helvetica",100)#yazı yazdırmak için font ayarlarını yapıyorum.

satesgame=font.render("SATES GAME",1,(255,255,255),(0,0,0))


while True: #bu döngü sayesinde pencereyi açık tutuyoruz.
    for event in pygame.event.get(): #pygame eventlerden yani olaylardan oluşur.
        if event.type==pygame.QUIT:sys.exit() #burda eğer birisi x tuşuna bastıysa sayfayı kapat diyoruz.

    pencere.blit(satesgame, (175,250)) #yazımızı ekranda göstermek için yazdığımız bir kod
    pygame.display.update()


