import pygame
from random import randint, choice

class Robotti:
    def __init__(self):
        pygame.init()
 
        self.naytto = pygame.display.set_mode((640, 480))
        pygame.display.set_caption(88*" "+"Robotti")
        self.fontti = pygame.font.SysFont("Arial", 24)
        self.kello = pygame.time.Clock()
 
        pygame.draw.line(self.naytto, (0, 0, 255), (2, 478), (638, 478), 4)
        pygame.draw.line(self.naytto, (0, 0, 255), (2, 2), (638, 2), 4)
        pygame.draw.line(self.naytto, (0, 0, 255), (2, 2), (2, 478), 4)
        pygame.draw.line(self.naytto, (0, 0, 255), (638, 2), (638, 478), 4)
 
        self.oikealle = False
        self.vasemmalle = False
        self.ylos = False
        self.alas = False
 
        self.robo = pygame.image.load("robo.png")
        self.x = 20
        self.y = 20
 
        self.haamu = pygame.image.load("hirvio.png")
        self.haamut = []
 
        self.kolikko = pygame.image.load("kolikko.png")
        self.kolikot = {}
 
        self.pisteet = 0
        self.level = 0
 
        self.silmukka()
 
    def silmukka(self):
        while True:
            if self.kolikot == {} and self.level != -1:
                self.level += 1
                self.uusi_kentta(self.level)
            if self.level == -1:
                self.pelin_loppu()
                self.ohjaus()
            else:
                self.ohjaus()
                self.tapahtumat()
                self.piirra_naytto()
                self.kello.tick(60)
 
    def uusi_kentta(self, kentta: int):
        self.x = 20
        self.y = 20
 
        if kentta == 1:
            self.pisteet = 0
        self.haamut = self.generoi_viholliset(kentta)
        self.kolikot = self.generoi_kolikot(kentta)
 
    def generoi_viholliset(self, kentta: int):
        haamu = pygame.image.load("hirvio.png")
        haamut = []
        if kentta == 1:
            for i in range(0, 6):
                x_1 = randint(100, (630 - haamu.get_width()))
                y_1 = randint(100, 470 - haamu.get_height())
                nopeus = choice([-3,-2,-1,1,2,3])
                suunta = choice(["h", "v"])
                haamut.append([int(x_1), int(y_1), nopeus, suunta])
            return haamut
        elif kentta == 2:
            for i in range(0, 7):
                x_2 = randint(100, (630 - haamu.get_width()))
                y_2 = randint(100, 470 - haamu.get_height())
                nopeus = choice([-3,-2,-1,1,2,3])
                suunta = choice(["h", "v"])
                haamut.append([int(x_2), int(y_2), nopeus, suunta])
            return haamut
        elif kentta == 3:
            koko = haamu.get_size()
            self.haamu = pygame.transform.scale(haamu, (int(koko[0]*2), int(koko[1]*2)))
            for i in range(0, 4):
                x_3 = randint(100, (620 - self.haamu.get_width()))
                y_3 = randint(100, 460 - self.haamu.get_height())
                nopeus = choice([-2,-1,1,2])
                suunta = choice(["h", "v"])
                haamut.append([int(x_3), int(y_3), nopeus, suunta])
            return haamut
 
    def generoi_kolikot(self, kentta: int):
        kolikot = {}
        for i in range(0, 7):
            x_k = randint(100, (635 - self.kolikko.get_width()))
            y_k = randint(100, 475 - self.kolikko.get_height())
            kolikot[i] = (int(x_k), int(y_k))
        return kolikot
        
    def ohjaus(self):
        for tapahtuma in pygame.event.get():
            if self.level != -1:
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_LEFT:
                        self.vasemmalle = True
                    if tapahtuma.key == pygame.K_RIGHT:
                        self.oikealle = True
                    if tapahtuma.key == pygame.K_UP:
                        self.ylos = True
                    if tapahtuma.key == pygame.K_DOWN:
                        self.alas = True
 
                if tapahtuma.type == pygame.KEYUP:
                    if tapahtuma.key == pygame.K_LEFT:
                        self.vasemmalle = False
                    if tapahtuma.key == pygame.K_RIGHT:
                        self.oikealle = False
                    if tapahtuma.key == pygame.K_UP:
                        self.ylos = False
                    if tapahtuma.key == pygame.K_DOWN:
                        self.alas = False
            else:
                self.vasemmalle = False
                self.oikealle = False
                self.ylos = False
                self.alas = False                
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_p:
                    exit()
                if tapahtuma.key == pygame.K_u:
                    Robotti()
 
            if tapahtuma.type == pygame.KEYUP and self.level != -1:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = False
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = False
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = False
 
            if tapahtuma.type == pygame.QUIT:
                exit()
 
    def tapahtumat(self):
 
        if self.oikealle:
            if self.x <= 638 - self.robo.get_width():
                self.x += 2
        if self.vasemmalle:
            if self.x >= 1:
                self.x -= 2
        if self.ylos:
            if self.y >= 2:
                self.y -= 2
        if self.alas:
            if self.y <= 475 - self.robo.get_height():
                self.y += 2
 
        #haamujen kääntyminen seinään osuessa
        for i in range(0, len(self.haamut)):
            if self.haamut[i][0] + self.haamu.get_width() > 630 or self.haamut[i][0] < 10: 
                self.haamut[i][2] = -1 * self.haamut[i][2]
            if self.haamut[i][1] + self.haamu.get_height() > 470 or self.haamut[i][1] < 10: 
                self.haamut[i][2] = -1 * self.haamut[i][2]
            if self.haamut[i][0] + self.haamu.get_width() <= 633 and self.haamut[i][0] >= 3 and self.haamut[i][3] == "h":
                self.haamut[i][0] += int(self.haamut[i][2])
            elif self.haamut[i][1] + self.haamu.get_height() <= 473 and self.haamut[i][1] >= 3 and self.haamut[i][3] == "v":    
                self.haamut[i][1] += int(self.haamut[i][2])
 
        #määritetään robotin rajakoordinaatit
        robo_rajat = []
        for i in range(self.x, self.x + self.robo.get_width()):
            robo_rajat.append((i, self.y))
            robo_rajat.append((i, self.y + self.robo.get_height()))
        for i in range(self.y, self.y + self.robo.get_height()):
            robo_rajat.append((self.x, i))
            robo_rajat.append((self.x + self.robo.get_width(), i))
        robo_rajat = list(dict.fromkeys(robo_rajat))
 
        
        #määritetään haamujen reunapisteet
        haamu_rajat = []
        for i in self.haamut:
            if self.level == 3:
                for j in range(0,40,5):
                    haamu_rajat.append((i[0] + j + 30, i[1] + j + 30))
                    haamu_rajat.append((i[0] + self.haamu.get_width() - j - 10, i[1] +j + 10))
                    haamu_rajat.append((i[0] + j + 10, i[1] + self.haamu.get_height() - j - 10))
                    haamu_rajat.append((i[0] + self.haamu.get_width() - 10 - j, i[1] + self.haamu.get_height()- 10 - j))
            else:
                for j in range(0,4):
                    haamu_rajat.append((i[0] + j + 10, i[1] + j + 10))
                    haamu_rajat.append((i[0] + self.haamu.get_width() - j - 10, i[1] +j + 10))
                    haamu_rajat.append((i[0] + j + 10, i[1] + self.haamu.get_height() - j - 10))
                    haamu_rajat.append((i[0] + self.haamu.get_width() - 10 - j, i[1] + self.haamu.get_height()- 10 - j))
 
 
        #määritetään kolikkojen reunapisteet
        kolikko_rajat = []
        for i in self.kolikot:
            for j in range(0,4):
                kolikko_rajat.append((i, (+j, self.kolikot[i][1]+j)))
                kolikko_rajat.append((i, (self.kolikot[i][0] + self.kolikko.get_width() - j, self.kolikot[i][1] + j)))
                kolikko_rajat.append((i, (self.kolikot[i][0] + j, self.kolikot[i][1] + self.kolikko.get_height() - j)))
                kolikko_rajat.append((i, (self.kolikot[i][0] + self.kolikko.get_width() - j, self.kolikot[i][1] + self.kolikko.get_height() - j)))
        kolikko_rajat = list(dict.fromkeys(kolikko_rajat))
 
        #verrataan robotin rajoja haamujen ja kolikoiden reunapisteisiin eli sitä onko pelaaja osanut haamuihin/kolikoihin
        haamu_osumat = [tuple for tuple in robo_rajat if tuple in haamu_rajat]
        if haamu_osumat != []:
            self.level = -1
 
        kolikko_osumat = []
        for i in robo_rajat:
            for j in kolikko_rajat:
                if i == j[1]:
                    self.kolikot[j[0]] = (j[0], 1000, 1000)
                    if j[0] not in kolikko_osumat:
                        kolikko_osumat.append(j[0])
        for i in kolikko_osumat:
            if i in self.kolikot:
                self.kolikot.pop(i)
        self.pisteet += int(len(kolikko_osumat))
        if self.pisteet == 21:
            self.level = -1
            self.pelin_loppu()
                
    def piirra_naytto(self):
        if self.level == -1:
            self.pelin_loppu()
        else:
            self.naytto.fill((255, 255, 255), (4, 4, 630, 470))
            self.naytto.blit(self.robo, (self.x, self.y))
            for i in self.haamut:
                self.naytto.blit(self.haamu, (i[0], i[1]))
            for i in self.kolikot:
                self.naytto.blit(self.kolikko, (self.kolikot[i][0], self.kolikot[i][1]))
            teksti = self.fontti.render(f"Pisteet: {self.pisteet}", True, (255, 0, 0))
            self.naytto.blit(teksti, (500, 5))
            pygame.display.flip()
 
    def pelin_loppu(self):
        self.kello.tick(0)
        self.naytto.fill((0,0,102))
        pygame.draw.rect(self.naytto, (0,0,102), (0, 0, 640, 480))
        fontti = pygame.font.SysFont("Arial", 24)
        if self.pisteet == 21:
            gameover = fontti.render(f"Peli läpäisty! pisteet: {self.pisteet}", True, (255, 0, 0))
            jattirobo = pygame.transform.scale(self.robo, (int(300), int(500)))
            self.naytto.blit(jattirobo, (0, 0))
        else:
            gameover = fontti.render(f"Peli päättyi! pisteet: {self.pisteet}", True, (255, 0, 0))
            jattihaamu = pygame.transform.scale(self.haamu, (int(300), int(500)))
            self.naytto.blit(jattihaamu, (0, 0))
        self.naytto.blit(gameover, (300, 220))
        uusipeli = fontti.render("U = uusi peli, P = poistu", True, (255, 0, 0))
        self.naytto.blit(uusipeli, (300, 260))
        pygame.display.flip()
 
 
if __name__ == "__main__":
    Robotti()