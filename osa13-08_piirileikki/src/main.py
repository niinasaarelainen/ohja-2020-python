import pygame, math

# Läpällä treenattu audiota: pygame.mixer.music.play  ja   pygame.mixer.Sound

class Robotti:

    def __init__(self, alku_x, alku_y, kulma):
        self.x = alku_x
        self.y = alku_y
        self.kulma = kulma

    def pyori(self):
        self.kulma += 0.01
        self.x = 320+math.cos(self.kulma)*piirin_koko -robo.get_width()/2
        self.y = 240+math.sin(self.kulma)*piirin_koko -robo.get_height()/2
        


pygame.init()
naytto = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Piirileikki")

robo = pygame.image.load("robo.png")
piirin_koko = 140

kulma = 0
robotit = []
for i in range(10):
    x = 320 + math.cos(kulma) * piirin_koko - robo.get_width()/2
    y = 240 + math.sin(kulma) * piirin_koko - robo.get_height()/2
    robotit.append(Robotti(x, y, kulma))
    kulma += 2* math.pi / 10

kello = pygame.time.Clock()

pygame.mixer.music.load('robo.wav')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)                 # -1 = loop
robo_sound = pygame.mixer.Sound('robo.wav')

uusi_robotti_sound = 0

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
    naytto.fill((0, 0, 0))

    uusi_robotti_sound += 1
    if uusi_robotti_sound % 500 == 0:        
        robo_sound.play()               # tämä ei looppaa

    for r in robotit:
        r.pyori()
        naytto.blit(robo, (r.x, r.y)) 

    pygame.display.flip()     
    kello.tick(80)
