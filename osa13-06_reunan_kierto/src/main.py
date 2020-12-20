import pygame


pygame.init()

naytto = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Reunan kierto")
robo = pygame.image.load("robo.png")

x = 0
y = 0
nopeus = 2      # koodattu niin sukasti että ei toimi esim nopeudella 4 !!!
kello = pygame.time.Clock()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))

    # oikealle:
    if x+robo.get_width() < 640 and y == 0 :
        x += nopeus
    # alas:  
    elif x == 640-robo.get_width() and y+robo.get_height() < 480 :
        y += nopeus
    # vasemmalle:
    elif x > 0 and y+robo.get_height() == 480 :
        x -= nopeus
    # ylös:
    elif x == 0 and y > 0:
        y -= nopeus
    
    pygame.display.flip()      
    kello.tick(60)


