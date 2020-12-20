import pygame, random

# robotit: jatkuvasti satunnainen määrä ja sijainti

class Robotti:

    def __init__(self):
        self.x = random.randint(0, WIDTH - robo.get_width())
        self.y = 0 - robo.get_height()
        self.nopeus = 3
        self.nakyvilla = True   # vain näkyvillä olevia robotteja liikutellaan while True:ssa

    def liiku(self):        
        if self.y + robo.get_height() == HEIGHT:           
            if self.x < int(WIDTH / 2):
                 self.x -= self.nopeus
            else:
                 self.x += self.nopeus
        else:
             self.y += self.nopeus
                
        if self.x < 0 - robo.get_width() or self.x > WIDTH:    
             self.nakyvilla = False



pygame.init()
kello = pygame.time.Clock()

HEIGHT = 480
WIDTH = 640
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robotti-invaasio")

robo = pygame.image.load("robo.png")
pygame.mixer.music.load("we_are_the_robots.ogg")       # .ogg toimii
pygame.mixer.music.play(-1)

robotit = []

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
    naytto.fill((0, 0, 0))      
    tuleeko_robotti = random.randint(0,30)
    if tuleeko_robotti == 30:
        robotit.append(Robotti())
    for robotti in robotit:
        if robotti.nakyvilla:
            robotti.liiku()
            naytto.blit(robo, (robotti.x, robotti.y))
        else:
            robotit.remove(robotti)

    pygame.display.flip()     
    kello.tick(60)
