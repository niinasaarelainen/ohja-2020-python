import pygame, random

class Robotti:   # ohjataan nuolinäppäimillä

    def __init__(self):
        self.x = int(WIDTH/2)
        self.y = HEIGHT-robo.get_height()
        self.nopeus = 4
        self.oikealle = False           
        self.vasemmalle = False
        self.robon_oik_reuna = robo.get_width() - 10 # - 10 = robossa mustaa reunoissa 
   
    def key_events(self, tapahtuma):
        if tapahtuma.type == pygame.KEYDOWN:      # parempi kuin scancode
            if tapahtuma.key == pygame.K_RIGHT:
                self.oikealle = True
            if tapahtuma.key ==  pygame.K_LEFT:
                self.vasemmalle = True
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key ==  pygame.K_RIGHT:
                self.oikealle = False
            if tapahtuma.key ==  pygame.K_LEFT:
                self.vasemmalle = False
                
    def liiku(self):
        if self.oikealle and self.x <= WIDTH - self.robon_oik_reuna - self.nopeus:
            self.x += self.nopeus   
        if self.vasemmalle and self.x >= self.nopeus:
            self.x -= self.nopeus

#######################################################################################     

class Asteroidi:  # tippuilevat randomisti
    
    def __init__(self):
        self.x = random.randint(0, WIDTH - ast.get_width())  
        self.y = - 6    # -6 = kuvassa reunat jossa ei asteroidia
        self.nopeus = 1
        self.nakyvilla = True
        self.gameover = False
    
    def liiku(self):
        self.y += self.nopeus
        if self.y + ast.get_height() >= HEIGHT:
            self.gameover = True
        return self.gameover

    def onko_tormays(self, robon_x, robon_y):   
        asteroidin_oik_reuna = self.x + ast.get_width() - 13  # kuvassa reunat jossa ei asteroidia
        asteroidin_alareuna = self.y + ast.get_height() - 6
        robon_oik_reuna = robon_x + robo.get_width() - 5
        # asteroidin y:n alapositiota ei tartte, koska self.gameover liiku()-funktiossa
        if asteroidin_oik_reuna >= robon_x + 6 and self.x <= robon_oik_reuna and asteroidin_alareuna >= robon_y :
            self.nakyvilla = False
        return not self.nakyvilla 


#######################################################################################

def game_over():
    fontti_iso = pygame.font.SysFont("Arial", 64)
    teksti = fontti_iso.render("Game Over", True, (205, 205, 205))
    naytto.blit(teksti, (140, 140))
    
    teksti = fontti.render(f"Score: {pisteet}", True, (205, 205, 205))
    naytto.blit(teksti, (260, 220))
    pygame.display.update()
    
    while True:
       for event in pygame.event.get():            
          if event.type == pygame.QUIT:
             pygame.quit()

               

pygame.init()
WIDTH = 650
HEIGHT = 450
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroidit")

robo = pygame.image.load("robo.png")
ast = pygame.image.load("asteroidi.png").convert_alpha()
ast = pygame.transform.scale(ast, (60, 70))                     # resize = scale

kello = pygame.time.Clock()
pisteet = 0
fontti = pygame.font.SysFont("Arial", 24)

r = Robotti()
asteroidit = []
pygame.mouse.set_pos([WIDTH+1, HEIGHT+1])  # hiiri pois ruudulta


while True:
    
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
        r.key_events(tapahtuma)

    naytto.fill((0, 0, 0))          
    r.liiku()      
    naytto.blit(robo, (r.x, r.y))
    
    tuleeko_asteroidi = random.randint(0, 110)                               
    if tuleeko_asteroidi == 0 and len(asteroidit) <= 5:  # ei yli kuutta kerralla
        print(len(asteroidit))
        asteroidit.append(Asteroidi())

    if len(asteroidit) == 0:  # vähintään yksi ruudulla
        asteroidit.append(Asteroidi())
        
    for asteroidi in asteroidit:        
        if asteroidi.gameover:   # asteroidi osuu maahan
            game_over()
        if asteroidi.nakyvilla:
            asteroidi.liiku()
            if asteroidi.onko_tormays(r.x, r.y):
                pisteet += 1
        else:
            asteroidit.remove(asteroidi)   # tämä pitää tehdä, muuten asteroidi jää jököttämään roboton pään päälle
        naytto.blit(ast, (asteroidi.x, asteroidi.y))
         
    
    pist = "Pisteet: " + str(pisteet)
    teksti = fontti.render(pist, True, (255, 0, 0))
    naytto.blit(teksti, (510, 40))

    pygame.display.flip()     
    kello.tick(70)

