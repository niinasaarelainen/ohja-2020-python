import pygame

class Robotti:
    def __init__(self, alku_x, alku_y, ohjaimet):
        self.x = alku_x
        self.y = alku_y
        self.nopeus = 5
        self.aseta_ohjaimet(ohjaimet)
        self.ylos = False
        self.oikealle = False
        self.alas = False
        self.vasemmalle = False        

    def aseta_ohjaimet(self, ohjaimet):
        self.up = ohjaimet[0]
        self.right = ohjaimet[1]
        self.down = ohjaimet[2]
        self.left = ohjaimet[3]

    def key_events(self, tapahtuma):
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == self.right:
                self.oikealle = True
            if tapahtuma.key == self.left:
                self.vasemmalle = True
            if tapahtuma.key == self.down:
                self.alas = True
            if tapahtuma.key == self.up:
                self.ylos = True

        if tapahtuma.type == pygame.KEYUP:           
            if tapahtuma.key == self.right:
                self.oikealle = False
            if tapahtuma.key == self.left:
                self.vasemmalle = False
            if tapahtuma.key == self.down:
                self.alas = False
            if tapahtuma.key == self.up:
                self.ylos = False

            """   scancodet
            if tapahtuma.scancode == self.right:
                self.oikealle = True
            if tapahtuma.scancode == self.left:
                self.vasemmalle = True
            if tapahtuma.scancode == self.down:
                self.alas = True
            if tapahtuma.scancode == self.up:
                self.ylos = True
            
            if tapahtuma.scancode == self.right:
                self.oikealle = False
            if tapahtuma.scancode == self.left:
                self.vasemmalle = False
            if tapahtuma.scancode == self.down:
                self.alas = False
            if tapahtuma.scancode == self.up:
                self.ylos = False
            """
            

    def liiku(self):        
        if self.oikealle:
            if self.x <= 640 - robon_leveys -self.nopeus:
                self.x += self.nopeus   
        if self.vasemmalle:
            if self.x >= self.nopeus:
                self.x -= self.nopeus
        if self.alas:
            if self.y <= 480 - robon_korkeus -self.nopeus:
                self.y += self.nopeus
        if self.ylos:
            if self.y >= self.nopeus:
                self.y -= self.nopeus      
                
                    
pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
robon_leveys = robo.get_width()
robon_korkeus = robo.get_height()

ohjaimet_pelaaja1 = [pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT]    # nuolet
ohjaimet_pelaaja2 = [ord("w"), ord("d"), ord("s"), ord("a")]    

r1 = Robotti(10, 10, ohjaimet_pelaaja1)
r2 = Robotti(100, 100, ohjaimet_pelaaja2)

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
        r1.key_events(tapahtuma)
        r2.key_events(tapahtuma)        

        
    naytto.fill((0, 0, 0))
    r1.liiku()       # huom! tämä ei saa olla for-loopin sisällä !!!!!  
    naytto.blit(robo, (r1.x, r1.y))
    r2.liiku()         
    naytto.blit(robo, (r2.x, r2.y))
    
    pygame.display.flip()
    kello.tick(50)
