from random import choice
import pygame
 
class Ammus:
    def __init__(self, x: int, y: int, kohde_x: int, kohde_y: int):
        self.x = x
        self.y = y
        self.x_nopeus = kohde_x-x
        self.y_nopeus = kohde_y-y
    
    def liike(self):
        suurempi = max(abs(self.x_nopeus), abs(self.y_nopeus))
        if suurempi == 0:
            suurempi = 1
        self.x += self.x_nopeus/suurempi*5
        self.y += self.y_nopeus/suurempi*5
 
    #osuuko robottiin?
    def osuma(self, robot: list, robo_leveys: int, robo_korkeus: int, peli):
        for robo in robot:
            if robo.x <= self.x <= robo.x+robo_leveys-4 and robo.y <= self.y <= robo.y+robo_korkeus-4:
                robot.pop(robot.index(robo))
                if self in peli.ammukset:
                    peli.ammukset.pop(peli.ammukset.index(self))
                peli.pisteet += 1
 
class Robotti:
    def __init__(self, paikka: tuple):
        self.x = paikka[0]
        self.y = paikka[1]
        if self.x < 0:
            self.suunta = "vaaka"
        else:
            self.suunta = "pysty"
        self.nopeus = choice([1,1.5,2,2.5])
    
    def liike(self):
        if self.suunta == "vaaka":
            self.x += self.nopeus
        else:
            self.y += self.nopeus
    
    #osuuko pelaajaan?
    def osuma(self, pelaaja_x: int, pelaaja_y: int, robo_leveys: int, pelaaja_leveys: int, robo_korkeus: int, pelaaja_korkeus: int, peli):
        if (pelaaja_x-robo_leveys+9 <= self.x <= pelaaja_x+pelaaja_leveys-12) and (pelaaja_y-robo_korkeus+4 <= self.y <= pelaaja_y+pelaaja_korkeus-3):
            peli.peli_kaynnissa = False
            peli.game_over = True
 
 
class Peli:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("BLOB ON THE RUN")
        self.kello = pygame.time.Clock()
        self.roboajastin = 50
 
        self.peli_kaynnissa = False
        self.game_over = False
        self.voitto = False
 
        self.hirvio = pygame.image.load("hirvio.png")
        self.robo = pygame.image.load("robo.png")
        self.naytto = pygame.display.set_mode((640, 480))
 
        self.x = 320-self.hirvio.get_width()/2
        self.y = 240-self.hirvio.get_height()/2
        self.oikealle = False
        self.vasemmalle = False
        self.ylos = False
        self.alas = False
        self.hiiri_x = 0
        self.hiiri_y = 0
 
        self.pisteet = 0
        self.ammukset = []
        self.robotit = []
        robo_etaisyys_x = (640-20-self.robo.get_width())/4
        robo_etaisyys_y = (480-20-self.robo.get_height())/3
        robo_x_paikat = [(10+robo_etaisyys_x*i, -self.robo.get_height()) for i in range(5)]
        robo_y_paikat = [(-self.robo.get_width(), 10+robo_etaisyys_y*i) for i in range(4)]
        self.robo_paikat = robo_x_paikat+robo_y_paikat
 
        self.silmukka()
 
    def silmukka(self):
        while True:
            self.tapahtumat()
 
            #voitto
            if self.pisteet >= 100 and self.robotit == []:
                if not self.voitto:
                    self.voitto = True
                    self.peli_kaynnissa = False
                if self.y <= 550:
                    self.y += 2
 
            if self.peli_kaynnissa:
                #pelaajan liike
                if self.oikealle and self.x <= 640-self.hirvio.get_width():
                    self.x += 3
                if self.vasemmalle and self.x >= -4:
                    self.x -= 3
                if self.ylos and self.y >= -2:
                    self.y -= 3
                if self.alas and self.y <= 480-self.hirvio.get_height(): 
                    self.y += 3
                
                #ammukset
                for ammus in self.ammukset:
                    if 0 <= ammus.x <= 640 and 0 <= ammus.y <= 480:
                        ammus.liike()
                        ammus.osuma(self.robotit, self.robo.get_width(), self.robo.get_height(), self)
                    else:
                        self.ammukset.pop(self.ammukset.index(ammus))
                
                #robotit
                self.roboajastin += 1
                if self.pisteet <= 14:
                    if self.roboajastin % (100) == 0:
                        self.robotit.append(Robotti(choice(self.robo_paikat)))
                elif 15 <= self.pisteet <= 39:
                    if self.roboajastin % (50) == 0:
                        self.robotit.append(Robotti(choice(self.robo_paikat)))
                elif 40 <= self.pisteet <= 59:
                    if self.roboajastin % (25) == 0:
                        self.robotit.append(Robotti(choice(self.robo_paikat)))
                elif 60 <= self.pisteet <= 100:
                    if self.roboajastin % (15) == 0:
                        self.robotit.append(Robotti(choice(self.robo_paikat)))
                for robotti in self.robotit:
                    if -50 <= robotti.x <= 640 and -100 <= robotti.y <= 480:
                        robotti.liike()
                        robotti.osuma(self.x, self.y,self.robo.get_width(), self.hirvio.get_width(),self.robo.get_height(), self.hirvio.get_height(), self)
                    else:
                        self.robotit.pop(self.robotit.index(robotti))
 
            self.piirra_naytto()
            self.kello.tick(60)
 
    def tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            
            #liike
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT or tapahtuma.key == pygame.K_a:
                    self.vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT or tapahtuma.key == pygame.K_d:
                    self.oikealle = True
                if tapahtuma.key == pygame.K_UP or tapahtuma.key == pygame.K_w:
                    self.ylos = True
                if tapahtuma.key == pygame.K_DOWN or tapahtuma.key == pygame.K_s:
                    self.alas = True
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT or tapahtuma.key == pygame.K_a:
                    self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT or tapahtuma.key == pygame.K_d:
                    self.oikealle = False
                if tapahtuma.key == pygame.K_UP or tapahtuma.key == pygame.K_w:
                    self.ylos = False
                if tapahtuma.key == pygame.K_DOWN or tapahtuma.key == pygame.K_s:
                    self.alas = False
            
            #hiiri
            if tapahtuma.type == pygame.MOUSEMOTION:
                self.hiiri_x = tapahtuma.pos[0]
                self.hiiri_y = tapahtuma.pos[1]
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN and not self.peli_kaynnissa and not self.game_over and not self.voitto:
                if 230 <= self.hiiri_x <= 410 and 390 <= self.hiiri_y <= 456:
                    self.peli_kaynnissa = True
            elif tapahtuma.type == pygame.MOUSEBUTTONDOWN and self.peli_kaynnissa:
                self.ammukset.append(Ammus(self.x + self.hirvio.get_width()/2, self.y + self.hirvio.get_height()/2, self.hiiri_x, self.hiiri_y))
 
    
    def piirra_naytto(self):
        self.naytto.fill((113,193,156))
 
        #peruspeli
        self.naytto.blit(self.hirvio, (self.x, self.y))
        for ammus in self.ammukset:
            pygame.draw.circle(self.naytto, (0,0,0), (ammus.x, ammus.y), 4)
        for robotti in self.robotit:
            self.naytto.blit(self.robo, (robotti.x, robotti.y))
        fontti = pygame.font.SysFont("Arial", 22)
        teksti = fontti.render(f"Score: {self.pisteet}", True, (0,0,0))
        self.naytto.blit(teksti, (630-teksti.get_width(), 10))
 
        #menu tekstit yms.
        if not self.peli_kaynnissa:
            fontti1 = pygame.font.SysFont("Arial", 26)
            fontti2 = pygame.font.SysFont("Arial", 18)
            fontti3 = pygame.font.SysFont("Arial", 12)
 
            if not self.game_over and not self.voitto:
                pelin_nimi = fontti1.render("BLOB ON THE RUN", True, (168,19,48))
                self.naytto.blit(pelin_nimi, ((640-pelin_nimi.get_width())/2, 70))
                kuvaus1 = fontti2.render("You have escaped from the lab but the security robots are on your tail!", True, (0,0,0))
                kuvaus2 = fontti2.render("Fight your way to freedom or be doomed to return to your imprisonment.", True, (0,0,0))
                self.naytto.blit(kuvaus1, ((640-kuvaus1.get_width())/2, 110))
                self.naytto.blit(kuvaus2, ((640-kuvaus2.get_width())/2, 130))
                ohjeet1 = fontti2.render("HOW TO PLAY: Gain points by shooting robots and don't let them get too close!", True, (0,0,0))
                ohjeet2 = fontti2.render("MOVE with arrow keys or WASD.", True, (0,0,0))
                ohjeet3 = fontti2.render("SHOOT by press any mouse button. The projectile will fly towards the position of the cursor.", True, (0,0,0))
                self.naytto.blit(ohjeet1, ((640-ohjeet1.get_width())/2, 300))
                self.naytto.blit(ohjeet2, ((640-ohjeet2.get_width())/2, 330))
                self.naytto.blit(ohjeet3, ((640-ohjeet3.get_width())/2, 360))
                button = fontti1.render("START GAME", True, (0,0,0))
                click = fontti3.render("(click here)", True, (50,50,50))
                pygame.draw.rect(self.naytto, (255,255,255), (230, 390, 180, 66))
                self.naytto.blit(button, ((640-button.get_width())/2, 400))
                self.naytto.blit(click, ((640-click.get_width())/2, 435))
            elif self.game_over and not self.voitto:
                game_over = fontti1.render("GAME OVER", True, (168,19,48))
                self.naytto.blit(game_over, ((640-game_over.get_width())/2, 150))
                text = fontti2.render("The robots caught you!", True, (168,19,48))
                self.naytto.blit(text, ((640-text.get_width())/2, 190))
            else:
                win = fontti1.render("YOU WIN!", True, (255,255,255))
                self.naytto.blit(win, ((640-win.get_width())/2, 150))
                text = fontti2.render("You managed to defeat the robots and escape the lab!", True, (255,255,255))
                self.naytto.blit(text, ((640-text.get_width())/2, 190))
 
        pygame.display.flip()
 
 
if __name__ == "__main__":
    Peli()