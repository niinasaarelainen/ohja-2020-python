import pygame, math
from datetime import datetime

class Viisari:

    def __init__(self, viisarin_pituus, nopeus, alkuaika, paksuus):
        self.viisarin_pituus = viisarin_pituus
        self.kulma = 2* math.pi / 60 * (alkuaika -15) # 0-kulma on varttia yli
        self.nopeus = nopeus
        self.paksuus = paksuus

    def liikuta(self):
        self.kulma += self.nopeus
        self.x = 320+math.cos(self.kulma)*self.viisarin_pituus
        self.y = 240+math.sin(self.kulma)*self.viisarin_pituus

    def koordinaatit(self):
        return self.x, self.y

#############################################################################################
class Kellonaika:
    def __init__(self):
        self.tunnit_str = datetime.now().strftime("%H")
        self.minuutit_str = datetime.now().strftime("%M")
        self.sekunnit_str = datetime.now().strftime("%S")

    def aika_ints(self):
        return (int(self.tunnit_str), int(self.minuutit_str), int(self.sekunnit_str))

    def aika_str(self):
        return datetime.now().strftime("%H:%M:%S")
    
#############################################################################################    

pygame.init()
WIDTH = 640
HEIGHT = 480
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
keskus = (int(WIDTH/2), int(HEIGHT/2))
sisainen_kello = pygame.time.Clock()

klo = Kellonaika()
h, m, s = klo.aika_ints()

sekuntiviisari = Viisari(190, 2 * math.pi / 60, s-1, 1)
minuuttiviisari = Viisari(180, 2 * math.pi / (60 * 60), m, 2)
tuntiviisari = Viisari(155, 2 * math.pi / (60 * 60 * 12), h * 5, 4) # *5 = esim klo 12 näyttää samalta kuin 60 min
viisarit = [sekuntiviisari, minuuttiviisari, tuntiviisari]

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()

    klo = Kellonaika()
    pygame.display.set_caption(klo.aika_str())
    
    naytto.fill((0, 0, 0)) 
    pygame.draw.circle(naytto, (255, 0, 0), keskus, 202)
    pygame.draw.circle(naytto, (0, 0, 0), keskus, 199)
    pygame.draw.circle(naytto, (255, 0, 0), keskus, 10)

    for viisari in viisarit:
        viisari.liikuta()
        pygame.draw.line(naytto, (0, 0, 255), (viisari.koordinaatit()), keskus, viisari.paksuus)    
                
    pygame.display.flip()     
    sisainen_kello.tick(1)
