import pygame
import time
from random import randint
 
class Roboviha:
    def __init__(self):
        pygame.init()
        #pelin tarkeat elementit
        self.keratyt_kolikot = 0
        self.kello = pygame.time.Clock()
        pygame.display.set_caption("Roboviha")
        self.alusta_peli()
        #ovi grafiikka
        self.ovi = pygame.image.load("ovi.png")
        #peli kaynnistyy
        self.pelin_aloitusnaytto()
        self.pelin_silmukka()
 
    def alusta_peli(self):
        #Alustaa pelin kaikki toiminnot
        self.naytto = pygame.display.set_mode((800, 800))
        self.alusta_ohjaimet()
        self.alusta_pelihahmo()
        self.alusta_robo()
        self.alusta_kolikko()
 
    def alusta_ohjaimet(self):
        #Alustaa pelin ohjaimet
        self.ylos = False
        self.alas = False
        self.oikealle = False
        self.vasemmalle = False
 
    def alusta_pelihahmo(self):
        #Alustaa pelihahmon
        self.hirvio = pygame.image.load("hirvio.png")
        self.hirvio_x = 150
        self.hirvio_y = 550
        self.hirvio_nopeus_x = 2
        self.hirvio_nopeus_y = 2
        self.hirvio_leveys = self.hirvio.get_width()
        self.hirvio_korkeus = self.hirvio.get_height()
 
    def alusta_robo(self):
        #Alustaa pelin vihollisen
        self.robo = pygame.image.load("robo.png")
        self.robo_x = 0
        self.robo_y = 0
        #Vihollisen suunta ja nopeus arvotaan ja peliin tulee lisaa yllatysta jos opintopisteita on enemman
        self.robo_nopeus_x = randint(2, 5+self.keratyt_kolikot)
        self.robo_nopeus_y = randint(1, 3+self.keratyt_kolikot)
        self.robo_leveys = self.robo.get_width()
        self.robo_korkeus = self.robo.get_height()
        self.robo_kaapattu = False
 
    def alusta_kolikko(self):
        #Alustaa opintopisteet
        self.kolikko = pygame.image.load("kolikko.png")
        self.kolikko_x = -50
        self.kolikko_y = -50
        self.kolikko_kaapattu = False
 
    def lopeta_peli(self):
        #Kun peli paattyy havioon
        fontti = pygame.font.SysFont("Arial", 20)
        fontti2 = pygame.font.SysFont("Arial", 50)
        self.naytto.fill((0, 0, 0))
        peli_ohi = fontti2.render("GAME OVER!", True, (0, 255, 0))
        self.naytto.blit(peli_ohi, (400- peli_ohi.get_width()/2, 300))
        peli_ohi2 = fontti.render("VOI EI ROBOTIT PÄÄSIVÄT PAINAJAISIISI!", True, (0, 255, 0))
        self.naytto.blit(peli_ohi2, (400- peli_ohi2.get_width()/2, 400))
        peli_ohi3 = fontti.render("NE SAATTAVAT OLLA TODELLA ARVAAMATTOMIA JA PILATA OPINTOSI!", True, (0, 255, 0))
        self.naytto.blit(peli_ohi3, (400- peli_ohi3.get_width()/2, 450))
        peli_ohi4 = fontti.render("VOIT VIELÄ YRITTÄÄ UUSINTAA! PELI KÄYNNISTYY NYT UUDELLEEN!", True, (0, 255, 0))
        self.naytto.blit(peli_ohi4, (400- peli_ohi4.get_width()/2, 500))
        pygame.display.flip()
        #Nuku 10sek ja peli kaynnistyy uudelleen
        time.sleep(10)
        Roboviha()
       
    def lopeta_peli_voittoon(self):
        #Kun peli paattyy voittoon
        fontti = pygame.font.SysFont("Arial", 20)
        fontti2 = pygame.font.SysFont("Arial", 50)
        self.naytto.fill((0, 0, 0))
        peli_ohi = fontti2.render("SINÄ ONNISTUIT!", True, (0, 255, 0))
        self.naytto.blit(peli_ohi, (400- peli_ohi.get_width()/2, 300))
        peli_ohi2 = fontti.render("KERÄSIT VIISI OPINTOPISTETTÄ JA PÄÄSET EROON ROBOTEISTA!", True, (0, 255, 0))
        self.naytto.blit(peli_ohi2, (400- peli_ohi2.get_width()/2, 400))
        peli_ohi3 = fontti.render("VOIT UUSIA KURSSIN! PELI KÄYNNISTYY NYT UUDELLEEN!", True, (0, 255, 0))
        self.naytto.blit(peli_ohi3, (400- peli_ohi3.get_width()/2, 450))
        pygame.display.flip()
        #Nuku 10sek ja peli kaynnistyy uudelleen
        time.sleep(10)
        Roboviha()
 
    def pelin_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            #Tapahtumat pelissa kaytettaville nappaimille
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_r:
                    self.pelin_silmukka()
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
                
            if tapahtuma.type == pygame.QUIT:
                exit()
 
 
 
    def pelin_aloitusnaytto(self):
        while True:
            self.pelin_tapahtumat()
            self.naytto.fill((0, 0, 0))
            fontti = pygame.font.SysFont("Arial", 17)
            fontti2 = pygame.font.SysFont("Arial", 50)
            #Luodaan alku informaatio ja pelin tarina
            rivi1 = fontti.render("VUODEN 2020 LOPPU HÄÄMÖTTÄÄ.", True, (0, 255, 0))
            self.naytto.blit(rivi1, (400 -rivi1.get_width()/2, 50))
            rivi2 = fontti.render("OLET OLLUT KOTONA LIIAN PITKÄÄN JA NÄYTÄT HAAMULTA.", True, (0, 255, 0))
            self.naytto.blit(rivi2, (400 -rivi2.get_width()/2, 100))
            rivi3 = fontti.render("KÄYT OHJELMOINNIN JATKOKURSSIA JA ALAT NÄHDÄ PAINAJAISIA ROBOTEISTA.", True, (0, 255, 0))
            self.naytto.blit(rivi3, (400 -rivi3.get_width()/2, 150))
            rivi4 = fontti.render("TEHTÄVÄSI ON VIEDÄ ROBOTIT POIS TALOSTASI NUOLINÄPPÄIMILLÄ.", True, (0, 255, 0))
            self.naytto.blit(rivi4, (400 -rivi4.get_width()/2, 200))
            rivi5 = fontti.render("JOKAISESTA ULOS HEITETYSTÄ ROBOTISTA SAAT OPINTOPISTEEN. TALLETA SE WEBOODIIN.", True, (0, 255, 0))
            self.naytto.blit(rivi5, (400 -rivi5.get_width()/2, 250))
            rivi6 = fontti.render("KERÄÄ VIISI OPINTOPISTETTÄ JA PÄÄSET EROON ROBOTEISTA LOPULLISESTI!", True, (0, 255, 0))
            self.naytto.blit(rivi6, (400 -rivi6.get_width()/2, 300))
            rivi7 = fontti.render("VARO ETTEIVÄT ROBOTIT PÄÄSE MAKUUHUONEESEEN JA SITÄ KAUTTA PAINAJAISIISI!", True, (0, 255, 0))
            self.naytto.blit(rivi7, (400 -rivi7.get_width()/2, 350))
 
            #Pelin aloituspainike
            aloita = fontti2.render("ALOITA PELI PAINAMALLA 'R'", True, (0, 255, 0))
            self.naytto.blit(aloita, (400- aloita.get_width()/2, 450))
 
            pygame.display.flip()
 
    def pelin_naytto(self):
        #Pohja
        self.naytto.fill((255, 255, 255))
        pygame.draw.rect(self.naytto, (0, 0, 0), (0, 650, 800, 800))
        pygame.draw.line(self.naytto, (150, 150, 150), (0, 650), (800, 650), 5)
        self.naytto.blit(self.ovi, (750, 10))
        #Kolikkografiikka
        fontti = pygame.font.SysFont("Arial", 30)
        ruoka_rahasto = fontti.render(f"OPINTOPISTEITÄ KERÄTTY: {self.keratyt_kolikot}", True, (0, 255, 0))
        self.naytto.blit(ruoka_rahasto, (400- ruoka_rahasto.get_width()/2, 700))
        #Makuuhuone
        fontti2 = pygame.font.SysFont("Arial", 15)
        makuuhuone = fontti2.render("MAKUUHUONE", True, (0, 0, 0))
        self.naytto.blit(makuuhuone, (15, 580))
        pygame.draw.line(self.naytto, (150, 150, 150), (0, 550), (150, 550), 2)
        pygame.draw.line(self.naytto, (150, 150, 150), (150, 550), (150, 650), 2)
        #Weboodi
        pygame.draw.circle(self.naytto, (255, 102, 0), (738, 588), 60)
        saastopossu = fontti2.render("WEBOODI", True, (0, 0, 0))
        self.naytto.blit(saastopossu, (700, 582))
        #Tietokone
        pygame.draw.line(self.naytto, (150, 150, 150), (0, 100), (100, 100), 2)
        pygame.draw.line(self.naytto, (150, 150, 150), (100, 100), (100, 0), 2)
        tietokone = fontti2.render("TIETOKONE", True, (0, 0, 0))
        self.naytto.blit(tietokone, (5, 20))
 
        #Hahmon liike ja kolikon kuvake
        if self.hirvio_x+self.hirvio_leveys < 800 and self.oikealle:
            self.hirvio_x += self.hirvio_nopeus_x
        if self.hirvio_x > 0 and self.vasemmalle:
            self.hirvio_x -= self.hirvio_nopeus_x
        if self.hirvio_y > 0 and self.ylos:
            self.hirvio_y -= self.hirvio_nopeus_y
        if self.hirvio_y+self.hirvio_korkeus < 650 and self.alas:
            self.hirvio_y += self.hirvio_nopeus_y
        self.naytto.blit(self.hirvio, (self.hirvio_x, self.hirvio_y))
        self.naytto.blit(self.kolikko, (self.kolikko_x, self.kolikko_y))
 
        #Robon liike
        self.robo_x += self.robo_nopeus_x
        self.robo_y += self.robo_nopeus_y
        if self.robo_x == 0 or self.robo_x+self.robo_leveys >= 800:
            self.robo_nopeus_x = -self.robo_nopeus_x
        if self.robo_y == 0 or self.robo_y+self.robo_korkeus >= 650:
            self.robo_nopeus_y = -self.robo_nopeus_y
        self.naytto.blit(self.robo, (self.robo_x, self.robo_y))
 
        #Robotin kiinniotto
        osuma_x = self.robo_x+self.robo_leveys >= self.hirvio_x and self.robo_x <= self.hirvio_x+self.hirvio_leveys
        osuma_y = self.robo_y+self.robo_korkeus >= self.hirvio_y and self.robo_y <= self.hirvio_y+self.hirvio_korkeus
        if osuma_x and osuma_y and self.robo_kaapattu == False and self.kolikko_kaapattu == False:
            self.robo_kaapattu = True
        if self.robo_kaapattu == True:
            self.robo_x = self.hirvio_x+15
            self.robo_y = self.hirvio_y-15
 
        #Robotin palautus ja Kolikon kiinniotto
        if self.robo_kaapattu == True and (self.robo_x >= 730 and self.robo_y <= 15):
            self.alusta_robo()
            self.kolikko_kaapattu = True        
        if self.kolikko_kaapattu == True:
            self.kolikko_x = self.hirvio_x
            self.kolikko_y = self.hirvio_y+20
 
        #Kolikon palautus ja uusi robotti laukaistaan matkaan
        if self.kolikko_kaapattu == True and (self.kolikko_x >= 700 and self.kolikko_y >= 550):
            self.alusta_kolikko()
            self.keratyt_kolikot += 1
        if self.robo_x <= 150 and self.robo_y >=500 and self.robo_kaapattu == False:
            self.lopeta_peli()
        if self.keratyt_kolikot == 5:
            self.lopeta_peli_voittoon()
 
        pygame.display.flip()
        self.kello.tick(60)
 
    def pelin_silmukka(self):
        while True:
            self.pelin_tapahtumat()
            self.pelin_naytto()
 
if __name__ == "__main__":
    Roboviha()