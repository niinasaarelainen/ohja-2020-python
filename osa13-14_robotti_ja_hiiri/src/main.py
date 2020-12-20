import pygame

# MOUSEBUTTONDOWN   ja    MOUSEMOTION !

pygame.init()
naytto = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Robotti ja hiiri")

robo = pygame.image.load("robo.png")


def seuraa():

    robo_x = 40
    robo_y = 40
    hiiri_x = 0
    hiiri_y = 0

    kello = pygame.time.Clock()

    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.MOUSEMOTION:
                hiiri_x = tapahtuma.pos[0]
                hiiri_y = tapahtuma.pos[1]
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
        naytto.fill((0, 0, 0))
        robo_x = hiiri_x -robo.get_width()/2
        robo_y = hiiri_y - robo.get_height()/2
        naytto.blit(robo, (robo_x, robo_y))
        pygame.display.flip()
        kello.tick(160)


seuraa()
