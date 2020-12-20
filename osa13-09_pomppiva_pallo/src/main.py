import pygame

# koodattu käyttäen draw.circle (ennenkuin minulla oli tehtäväpohjan .png-kuvaa)
# treenattu luokan käyttöä, jotta pallon voi helposti monistaa --> yleishyödyllisempi koodi

class Pallo:
    def __init__(self, alku_x, alku_y, p_koko):
        self.x = alku_x
        self.y = alku_y
        self.p_koko= int(p_koko / 2) + 1
        self.oikealle = alku_x < WIDTH - self.p_koko  # oik / vas   
        self.alas = alku_y < HEIGHT - self.p_koko     # alas / ylös
    
    def liiku(self):            
        if self.oikealle:
            self.x += 1
        if not self.oikealle:
            self.x -= 1
        if self.alas:                
            self.y += 1
        if not self.alas:
            self.y -= 1

        # reunat:            
        if self.x == WIDTH - self.p_koko:     # kokeiltu not self.oikealle ja ehtojen yhdistäminen __EI__ toimi !!
            self.oikealle = False
        if self.x == 0 + self.p_koko:
            self.oikealle = True
        if self.y == 0 + self.p_koko:   
            self.alas = True
        if self.y == HEIGHT - self.p_koko:
            self.alas = False

####################################################################################################                              
pygame.init()
WIDTH = 800
HEIGHT = 700
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

p_koko = 25
turkoosi = (8, 255, 255)
#pallot = [Pallo(350, HEIGHT, p_koko)]
pallot = [
    Pallo(0, 172, p_koko), Pallo(WIDTH, 72,  p_koko),
    Pallo(350, HEIGHT + 1, p_koko), Pallo(651, 650, p_koko)
]


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
        
    naytto.fill((0, 0, 0))
    for pallo in pallot:
        pallo.liiku()  
        pygame.draw.circle(naytto, turkoosi, (pallo.x , pallo.y), p_koko)

    pygame.display.flip()
    kello.tick(320)
