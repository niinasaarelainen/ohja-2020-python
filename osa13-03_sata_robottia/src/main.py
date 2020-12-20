import pygame

def sata():
    x_aloitus = 50
    y = 100
    for i in range(10):
        x = x_aloitus
        for j in range(10):
            naytto.blit(robo, (x, y))
            x += leveys -8   #  kuvan mustat reunat  pois osittain
        y += 20
        x_aloitus += 10

    
pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
leveys = robo.get_width()
korkeus = robo.get_height()

sata()

pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
           pygame.quit()