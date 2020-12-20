import pygame
from random import randint
 
class Robobobo:
    def __init__(self):
 
        pygame.init()
        pygame.display.set_caption("Robobobo")
        self.lataa_kuvat()
        self.pisteet=0 #nollataan pistemäärä pelin alussa
        self.hirvioita = 10 #hirviöiden lukumäärä, kasvaa tasolta toiselle siirryttäessä 15:sta
        self.kolikoita = 0 #kerättävien kolikoiden määrä, kasvaa tasolta seuraavalle siirryttäessä
        self.hirviot=[] #hirviöiden lähtösijainti arvotaan tähän listaan
        self.kolikot=[] #kolikoiden sijainnit listataan
        self.nopeus=30 #asetetaan alkunopeus pelille, eli on aluksi hyvin hidas ja vähän pätkiikin, nopeutetaan pelin edetessä
        self.nayton_korkeus = 540
        self.nayton_leveys = 640
        self.fontti = pygame.font.SysFont("Cooper Black", 24)
        self.naytto = pygame.display.set_mode((self.nayton_leveys, self.nayton_korkeus))
        self.kello=pygame.time.Clock()
        self.x=0        #robon sijainnin koordinaatit          
        self.y=480-self.robo.get_height()
        self.r=100 #asetetaan näytön rgb-väreille alkuasetus, tummennetaan taustaa pelin edetessä
        self.g=100
        self.b=100
        self.taso=0
        self.gameover=False
        self.uusi_peli()
        self.silmukka()
        
 
    def lataa_kuvat(self):
        self.robo=pygame.image.load("robo.png")
        self.kolikko=pygame.image.load("kolikko.png")
        self.ovi=pygame.image.load("ovi.png")
        self.hirvio=pygame.image.load("hirvio.png")     
         
 
    def uusi_taso(self,):
        self.apupisteet=0 #tarvitaan, jotta tiedetään, milloin siirrytään seuraavalle tasolle
        self.taso+=1
        self.nopeus+=5 #frameja jokaisella tasolla lisää, eli nopeus kasvaa myös pikku hiljaa
        if self.r>0:
            self.r-=10
            self.g-=10
            self.b-=10
       
        self.kolikoita +=5
      
        self.x2 = randint(0,640-self.ovi.get_width()) #arvotaan oven paikka
        self.y2 = randint(0,480-self.ovi.get_height())
 
 
        if len (self.hirviot)<15:      
            for i in range(self.hirvioita):
                x1 = randint(0,640-self.hirvio.get_width())   #arvotaan leveyssuunnassa kohta, josta hirviö lähtee tulemaan alaspäin
            
                y1 = - randint(5*i,2000)       #arvotaan myös hirviön aloituskohta pystysuunnassa
                self.hirviot.append([x1,y1])     #lisätään se listaan
 
        for i in range (self.kolikoita):
            x1 = randint(0,640-self.kolikko.get_width())   #arvotaan kolikoiden paikat alussa niin, että ne eivät ole robossa kiinni heti alkuun
            y1 = randint(0,480-self.kolikko.get_height())       
           
            self.kolikot.append([x1,y1])
                 
 
    
    def uusi_peli(self):
        self.pisteet=0 #nollataan pistemäärä pelin alussa
        self.hirvioita = 10 #hirviöiden lukumäärä, tasolta toiselle siirryttäessä, lukumäärä ja nopeus? lisääntyvät
        self.kolikoita = 0 #kerättävien kolikoiden määrä, kasvaa tasolta seuraavalle siirryttäessä
        self.hirviot=[] #hirviöiden lähtösijainti arvotaan tähän listaan
        self.kolikot=[] #kolikoiden sijainnit listataan
        self.nopeus=30 #asetetaan alkunopeus pelille, nopeutetaan pelin edetessä
        self.x=0        #robon sijainnin koordinaatit          
        self.y=480-self.robo.get_height()
        self.x1=0   #ovikuvan alkukoordinaatit
        self.y1=0
        self.r=100 #asetetaan näytön rgb-väreille alkuasetus, tummennetaan taustaa pelin edetessä
        self.g=100
        self.b=100
        self.taso=0     #sisältää tiedon, millä tasolla mennään
        self.naytto.fill((self.r, self.g, self.b))
        self.gameover=False     #muuttuja, jonka avulla pysäytetään pelin loputtua muut komennot kuin Esc=lopetus ja f2=uusi peli
        pygame.display.flip()
        self.uusi_taso()
 
        
 
        
 
    def silmukka(self):
       
        while True:
            self.tutki_tapahtumat()
          
           
 
    
    
    def tutki_tapahtumat(self):
     
        oikealle = False
        vasemmalle = False
        ylos=False
        alas=False
    
        while True:
            for tapahtuma in pygame.event.get():
                if not self.gameover:
                    if tapahtuma.type == pygame.KEYDOWN:
                    
                        if tapahtuma.key == pygame.K_LEFT:
                            vasemmalle = True
                        if tapahtuma.key == pygame.K_RIGHT:
                            oikealle = True
                        if tapahtuma.key==pygame.K_UP:
                            ylos=True
                        if tapahtuma.key==pygame.K_DOWN:
                            alas=True
                        if tapahtuma.key == pygame.K_F2:
                            self.uusi_peli()
                        if tapahtuma.key == pygame.K_ESCAPE:
                            exit()                    
                
                    if tapahtuma.type == pygame.KEYUP:
                        if tapahtuma.key == pygame.K_LEFT:
                            vasemmalle = False
                        if tapahtuma.key == pygame.K_RIGHT:
                            oikealle = False
                        if tapahtuma.key==pygame.K_UP:
                            ylos=False
                        if tapahtuma.key==pygame.K_DOWN:
                            alas=False
                else:
                    oikealle = False
                    vasemmalle = False
                    ylos=False
                    alas=False
 
                    if tapahtuma.type == pygame.KEYDOWN:
                        if tapahtuma.key == pygame.K_F2:
                            self.uusi_peli()
                        if tapahtuma.key == pygame.K_ESCAPE:
                            exit()    
 
 
                if tapahtuma.type == pygame.QUIT:
                    exit()
 
 
                
            if oikealle and self.x<640-self.robo.get_width():
                self.x += 4 #liikutetaan roboa 4 pikseliä kerrallaan
            if vasemmalle and self.x>0:
                self.x -= 4
            if ylos and self.y>0:
                self.y -= 4
            if alas and self.y<480-self.robo.get_height():
                self.y += 4
 
 
 
 
            for i in range(len(self.hirviot)):
                if self.hirviot[i][0]<=self.robo.get_width()+self.x-10 and self.x+10 <= self.hirviot[i][0]+self.hirvio.get_width() and self.y+self.robo.get_height()-10>self.hirviot[i][1] and self.y+10<self.hirviot[i][1]+self.hirvio.get_height(): #robo osuu hirviöön
           
 
 
                 
                    self.gameover=True
                    self.hirviot[i][1]+=1
   
       
             
                elif self.hirviot[i][1]>self.nayton_korkeus: #hirvio osuu alareunaan:
                    
                    self.hirviot[i][0]= randint(0,self.nayton_leveys-self.hirvio.get_width()) #arvotaan hirviölle uusi lähtöpaikka, eli siirretään se uuteen paikkaan
                    self.hirviot[i][1] = - randint(5*i,2000)
                else:
                    if self.taso%3==0: #joka kolmannella tasolla hirviöiden nopeus kasvaa tuplanopeudeksi
                        self.hirviot[i][1]+=2
 
                    else:
                        self.hirviot[i][1]+=1
 
            for i in range(len(self.kolikot)):
                if self.kolikot[i][0]<=self.robo.get_width()+self.x and self.x <= self.kolikot[i][0]+self.kolikko.get_width() and self.y+self.robo.get_height()>self.kolikot[i][1] and self.y<self.kolikot[i][1]+self.kolikko.get_height(): #robo osuu kolikkoon
                    self.pisteet+=1
                    self.apupisteet+=1
                    self.kolikot[i][0]=-100 #poistetaan kolikko näytöltä eli siirretään kolikko sivuun
 
 
            self.piirra_naytto()
            if self.apupisteet==self.kolikoita and self.taso>3:
                if self.x2<=self.robo.get_width()+self.x-15 and self.x+15 <= self.x2+self.ovi.get_width() and self.y+self.robo.get_height()-15>self.y2 and self.y+15<self.y2+self.ovi.get_height():
                    self.uusi_taso()
 
 
            elif self.apupisteet==self.kolikoita:    
                self.uusi_taso()
            self.kello.tick(self.nopeus) #täällä käytetään arvoa, joka kasvaa joka tasolla
                    
   
 
 
    def piirra_naytto(self):
        self.naytto.fill((self.r, self.g, self.b))
        self.naytto.blit(self.robo, (self.x, self.y))
        if self.apupisteet==self.kolikoita and self.taso>3:
     
            self.naytto.blit(self.ovi,(self.x2,self.y2))
        
        for i in range (len(self.hirviot)): #hirviöt näytölle
            self.naytto.blit(self.hirvio,(self.hirviot[i][0],self.hirviot[i][1]))
 
        for i in range (len(self.kolikot)):  #kolikot näytölle
            self.naytto.blit(self.kolikko,(self.kolikot[i][0],self.kolikot[i][1]))
        if self.gameover:
            lopputeksti = self.fontti.render("Game Over!! uusi peli= f2, lopetus=Esc", True, (255, 0, 0))
            pygame.draw.ellipse(self.naytto, (0, 0, 0), (50, 120, 530, 160))                
            self.naytto.blit(lopputeksti, (90, 180))
 
        teksti = self.fontti.render("Taso: "+str(self.taso)+"                         pisteet: " + str(self.pisteet), True, (250, 255, 10))
        pygame.draw.rect(self.naytto, (50, 20, 240), (0, 481, 640, 520))
        self.naytto.blit(teksti, (100, 485))
        
        pygame.display.flip()
        
 
if __name__ == "__main__":
    Robobobo()