# TEE RATKAISUSI TÄHÄN:
import pygame, random
  

pygame.init()
naytto = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Neljä seinää")

robo = pygame.image.load("robo.png")
robon_leveys = robo.get_width()
robon_korkeus = robo.get_height()
x = 0
y = 480-robo.get_height()

oikealle = False
vasemmalle = False
alas = False
ylos = False
vauhti = 5

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()

        elif tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_DOWN:
                alas = True
            if tapahtuma.key == pygame.K_UP:
                ylos = True

        elif tapahtuma.type == pygame.KEYUP:           
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_DOWN:
                alas = False
            if tapahtuma.key == pygame.K_UP:
                ylos = False
    
        
    if oikealle and x <= 640 - robon_leveys - vauhti :    #  ei saa mennä reunojen yli !
            x += vauhti   
    if vasemmalle and x >= 0 + vauhti:
            x -= vauhti
    if alas and y <= 480 - robon_korkeus - vauhti:
            y += vauhti
    if ylos and y >= 0 + vauhti:
            y -= vauhti
                
    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()
    kello.tick(50)
