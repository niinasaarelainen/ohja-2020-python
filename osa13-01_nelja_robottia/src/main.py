import pygame

def kulmat():
    naytto.blit(robo, (0, 0))
    naytto.blit(robo, (640-leveys, 0))
    naytto.blit(robo, (0, 480-korkeus))
    naytto.blit(robo, (640-leveys, 480-korkeus))


pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
leveys = robo.get_width()
korkeus = robo.get_height()

kulmat()

pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()   # exit() tekee ärsyttävän kysymysikkunan

