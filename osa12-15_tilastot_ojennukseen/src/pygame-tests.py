import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))


while True:
    for tapahtuma in pygame.event.get():
        print(tapahtuma)
        if tapahtuma.type == pygame.QUIT:
            exit()