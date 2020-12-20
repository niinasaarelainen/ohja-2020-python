import pygame, random

def satunnaiset():
    for i in range(1000):
        naytto.blit(robo, ((random.randint(0, 640-leveys), random.randint(0, 480-korkeus) )))
                    

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

leveys = robo.get_rect().size[0]   # sama kuin get_width()
korkeus = robo.get_rect().size[1]

satunnaiset()

pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()   # exit() tekee ärsyttävän kysymysikkunan