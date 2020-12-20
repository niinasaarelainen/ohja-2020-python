import pygame, random
from nuottipeli_yhteiset_F import *

#######################################################################################################
class Robotti:
    
    def __init__(self):    
        self.nollaa()
        self.pic = pygame.transform.scale(pygame.image.load("robo.png").convert_alpha(), (KUVAN_KOKO, KUVAN_KOKO))  

    def nollaa(self):
        self.x = WIDTH + 2    # ei näy 
        self.y = HEIGHT + 2

    def siirry_nappaimen_maaraamaan_paikkaan(self, key, x):
        self.y = ALIN_NUOTTI_Y - (key - 102) * VIIVOJEN_VALI // 2 - KUVAN_KOKO // 2 
        self.x = x
              
    def liiku(self):   # myöhemmin voi vaihtaa mielipidetttä että sittenkin liikkuu
        pass           # toinen syy tälle: voi sanoa kaikille oliolle kerralla: liiku() for-luupissa

#######################################################################################################
class Hirvio:
    
    def __init__(self):   
        self.nollaa()
        self.pic = pygame.transform.scale(pygame.image.load("hirvio.png").convert_alpha(), (KUVAN_KOKO, KUVAN_KOKO))      

    def nollaa(self):
        self.x = 60  # lähtöpiste vas. reuna
        self.y = YLIN_VIIVA_Y + 25        
        self.korjaa_y = 1

    def liiku(self):           
        self.x += 0.45  
        self.y += 0.6 * self.korjaa_y 

#######################################################################################################
class Nuotti:
    
    def __init__(self):  
        self.alin_nuotti = 0  #  F-avaimen ala-F
        self.ylin_nuotti = 1   # G  aluksi kysellään vain kahta nuottia, uusi level = uusi nuotti
        self.sanakirjat()          
        self.nollaa()   
        self.jess_no_teksti = ""   
        self.jess_x = 0
        self.jess_y = 0
        self.pic = pygame.transform.scale(pygame.image.load("kolikko.png").convert_alpha(), (KUVAN_KOKO, KUVAN_KOKO))  
      
    def nollaa(self):
        self.x = WIDTH - 80  # lähtöpiste oikeassa reunassa
        self.y = self.arvo_nuotti()

    def kasvata_ylarajaa(self):
        self.ylin_nuotti += 1
    
    def sanakirjat(self):             
        self.sijainnit = {}
        self.nimet = {}
        for i in range(5):
            self.nimet[i] = chr(102 + i)     # chr 102 = f           
            self.sijainnit[i] = ALIN_NUOTTI_Y - i * VIIVOJEN_VALI // 2 - KUVAN_KOKO // 2   # /2 = viivojen väliin myös nuotti        
        # nimet jotka eivät mene aakkosten mukaan:
        self.nimet[2]  = 'a'
        self.nimet[3]  = 'h'
        self.nimet[4]  = 'c'


    def arvo_nuotti(self):
        self.arvottu_indeksi = random.randint(self.alin_nuotti, self.ylin_nuotti)
        self.x = WIDTH - 60
        self.y = self.sijainnit[self.arvottu_indeksi] 
        return self.y   
    
    def nykyinen_nimi(self):
        return self.nimet[self.arvottu_indeksi]   
        
    def liiku(self):  
        self.x -= 1

#######################################################################################################