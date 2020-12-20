import pygame

class Robotti:

    def __init__(self, alku_x, alku_y, nopeus):
        self.x = alku_x
        self.y = alku_y
        self.nopeus = nopeus

    def liiku(self):
        self.x += self.nopeus
        if (self.nopeus > 0 and self.x+robo.get_width() >= 640) or (self.nopeus < 0 and self.x <= 0):
            self.nopeus = -self.nopeus


pygame.init()
naytto = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Kaksi robottia")

robo = pygame.image.load("robo.png")

r1 = Robotti(0, 40, 4)
r2 = Robotti(0, 200, 8)   # 8 = tuplanopeus verrattuna 4:een

kello = pygame.time.Clock()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
    naytto.fill((0, 0, 0))      

    r1.liiku()
    r2.liiku()
    naytto.blit(robo, (r1.x, r1.y))
    naytto.blit(robo, (r2.x, r2.y))    

    pygame.display.flip()     
    kello.tick(60)
