import pygame, random, pygame.midi

#######################################################################################################
class Robotti:
    
    def __init__(self):    
        self.nollaa()
        self.pic = pygame.transform.scale(pygame.image.load("robo.png").convert_alpha(), (KUVAN_KOKO, KUVAN_KOKO))  

    def nollaa(self):
        self.x = WIDTH + 2    # ei näy 
        self.y = HEIGHT + 2

    def siirry_nappaimen_maaraamaan_paikkaan(self, key):
        self.y = ALIN_NUOTTI_Y - (key - 99) * int(VIIVOJEN_VALI/2) - int(KUVAN_KOKO / 2) 
              
    def liiku(self):   # myöhemmin voi vaihtaa mielipidetttä että sittenkin liikkuu
        pass           # toinen syy tälle: voi sanoa kaikille oliolle kerralla: liiku() for-luupissa

#######################################################################################################
class Hirvio:
    
    def __init__(self):   
        self.nollaa()
        self.pic = pygame.transform.scale(pygame.image.load("hirvio.png").convert_alpha(), (KUVAN_KOKO, KUVAN_KOKO))      

    def nollaa(self):
        self.x = 60  # lähtöpiste vas. reuna
        self.y = YLIN_VIIVA_Y + 15        
        self.korjaa_y = 1

    def liiku(self):           
        self.x += 0.4 
        self.y += 0.5 * self.korjaa_y 

#######################################################################################################
class Nuotti:
    
    def __init__(self):  
        self.alin_nuotti = 0  # keski-c
        self.ylin_nuotti = 4   # g
        self.sanakirjat()          
        self.nollaa()           
        self.pic = pygame.transform.scale(pygame.image.load("kolikko.png").convert_alpha(), (KUVAN_KOKO, KUVAN_KOKO))  
      
    def nollaa(self):
        self.x = WIDTH - 80  # lähtöpiste oikeassa reunassa
        self.y = self.arvo_nuotti()
    
    def sanakirjat(self):             
        self.sijainnit = {}
        self.nimet = {}
        for i in range(5):
            self.nimet[i] = chr(99 + i)     # chr 99 = c           
            self.sijainnit[i] = ALIN_NUOTTI_Y - i * int(VIIVOJEN_VALI / 2) - int(KUVAN_KOKO / 2)   # /2 = viivojen väliin myös nuotti        

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

def alkuteksti():
    naytto.fill(tumma)
    tekstit = []
    tekstit.append("Laita kätesi valmiiksi näppäimille c, d, e, f, g.")
    tekstit.append("Ohjelma kyselee näitä viittä G-avaimen nuottia.")
    tekstit.append("Robotti nappaa nuotin jos painat oikeaa näppäintä.")
    tekstit.append("Saa vastata myös väärin, mutta oikea vastaus pitää ")
    tekstit.append("tulla ennenkuin hirviö nappaa kolikon.")
    tekstit.append("Paina nyt mitä tahansa, niin peli käynnistyy.")
    y = 90
    for teksti in tekstit:
        t = fontti_keski.render(teksti, True, keltainen)
        naytto.blit(t, (50, y))
        y += 45
    pygame.display.flip()

    while True:
        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            else:                
                if tapahtuma.type == pygame.KEYDOWN:     
                    return       

def nollaa_kaikki():
    for olio in oliot:
        olio.nollaa()   
    for nuotti in nuotit:
        nuotti.nollaa()

def midi_play(n, nykyinen_indeksi):
    #ei voi laskea systeemillä, esim. i+=2, koska välillä on puolisävelaskel välillä koko-
    midi_numbers = {0:60, 1:62, 2:64, 3:65, 4:67}    #60 = keski-c, 67 = g
    midi_out.note_off(midi_numbers[nykyinen_indeksi], 110)
    midi_out.note_on(midi_numbers[n], 110)
    

def lisataanko_vauhtia(pisteet):
    if pisteet % 12 == 0 and pisteet > 0:  #  0%12 == 0  
        return 25
    return 0


def pelitilan_tekstit(vaarin, pisteet, nuotti):
    teksti = fontti_iso.render(f"Pisteet: {pisteet}", True, turkoosi)
    naytto.blit(teksti, (600, 30))    
    if vaarin:                         
        teksti = fontti_keski.render(f"Väärin. Nuotti on: {nuotti.nykyinen_nimi() }", True, punainen)  
    else:
        teksti = fontti_keski.render("Nuotin nimi?", True, turkoosi)        
    naytto.blit(teksti, (230, 40))    


def nuottiviivasto(viivan_pit):
    for i in range(5):
        pygame.draw.line(naytto, keltainen, (VIIVASTON_ALKU_X, YLIN_VIIVA_Y + i * VIIVOJEN_VALI), (viivan_pit, YLIN_VIIVA_Y + i * VIIVOJEN_VALI), 4)


def gameover(pisteet):
    naytto.fill(tumma)
    hiscore(pisteet)
    pygame.display.update()
    pygame.time.delay(500)  # 1/2 sekunnin viive, jottei käyttäjän edellinen peli käynnistä tahattomasti uutta
    pygame.event.clear()
    while True:
        for event in pygame.event.get():
           if event.type == pygame.KEYDOWN:  # palaa main():iin
                return
           elif event.type == pygame.QUIT:
               pygame.quit()
               

def hiscore(pisteet):
    f = open("hiscore_nuotti.txt", "r")
    uudestaan = fontti_pieni_bold.render("uusi peli: mikä tahansa näppäin", 1, keltainen)   # uusi peli
    naytto.blit(uudestaan, (400 , HEIGHT - 60))

    top5 = [int(rivi.replace("\n", "")) for rivi in f]       

    if pisteet > top5[-1]:        
        top5.append(pisteet)        
        top5 = sorted(top5)
        top5.reverse()
        monesko = top5.index(pisteet) + 1
        monesko_str = {1:"paras !!!", 2:"toka !!", 3:"kolmas !", 4:"neljäs", 5:"viides"}
        text = fontti_iso.render(f"Olet {monesko_str[monesko]}", 1, turkoosi)
    else:
        text = fontti_iso.render("Ei riitä Top5:een:", 1, turkoosi)
    naytto.blit(text, (150, 60))

    y = 140    
    for rivi in top5[:5]:
        luku = fontti_iso.render(str(rivi), 1, turkoosi)
        naytto.blit(luku, (200, y))
        y += 40
        
    write_file(top5[:5])
    

def write_file(lista):
    with open("hiscore_nuotti.txt", "w") as tiedosto:
        for rivi in lista:
            tiedosto.write(str(rivi)+"\n")

#############################################################################################################
        
pygame.init()
pygame.display.set_caption("Tunnista nuotin nimi")

pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)
midi_out.set_instrument(10)   # GM 10 = Glockenspiel

fontti_iso = pygame.font.SysFont("Arial", 36)
fontti_keski = pygame.font.SysFont("Arial", 30)
fontti_pieni_bold = pygame.font.SysFont("Arial", 24, bold = True)

WIDTH = 790
HEIGHT = 410
VIIVASTON_ALKU_X = 50
VIIVOJEN_VALI = 50
YLIN_VIIVA_Y = 100      
ALIN_NUOTTI_Y = 350     
KUVAN_KOKO = 50

naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

tumma = (25, 25, 25)
turkoosi = (0, 205, 205)
punainen = (255, 0, 0)
keltainen = (255, 255, 0)

robotti = Robotti()
hirvio = Hirvio()
oliot = [robotti, hirvio]
nuotit = [Nuotti()]     # aluksi 1 nuotti, uusissa leveleissä lisää


def main():
    nuotit = [Nuotti()]      # poistetaan 2-levelin ylim.nuotit
    nollaa_kaikki()
    pisteet = 0
    level = 1
    vaarin = False
    vauhti = 90   # ticks
    jess_no_aika = 290    
    jess_no = -1   # jess = 1, no =0, ei kumpaakaan tekstiä = -1
    nuotit[0].arvo_nuotti()     # aluksi 1 nuotti
    nykyinen_indeksi = nuotit[0].arvottu_indeksi
    midi_play(nuotit[0].arvottu_indeksi, nykyinen_indeksi)  # soitettava ja sammutettava nuotti

    while True:
        for nuotti in nuotit:
            if hirvio.x + 18 >= nuotti.x  :     
                gameover(pisteet)
                main()

        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            else:                
                if tapahtuma.type == pygame.KEYDOWN:    
                    robotti.siirry_nappaimen_maaraamaan_paikkaan(tapahtuma.key)  

                    oikea_nuotti = None
                    oikeat_nuotit = [n for n in nuotit if chr(tapahtuma.key) == n.nykyinen_nimi()]          # voi olla useita samannimisiä näytöllä kerralla
                    if not oikeat_nuotit == []:
                        oikea_nuotti =  sorted(oikeat_nuotit, key =lambda nuotti: nuotti.x )[0]    # pienin x

                    if not oikea_nuotti == None:
                        pisteet += 1                                             # TODO 2-->20 
                        if pisteet == 2 and len(nuotit) == 1:    # miinuspist.takia voi tulla 2 pist. useasti    
                            level = 2                                          
                            nuotit.append(Nuotti())
                        if pisteet == 4 and len(nuotit) == 2:     
                            level = 3                                          
                            nuotit.append(Nuotti())
                        teksti = fontti_keski.render("JESS !", True, turkoosi)    
                        naytto.blit(teksti, (oikea_nuotti.x, oikea_nuotti.y + 50))    
                        naytto.blit(robotti.pic, (oikea_nuotti.x , robotti.y))  
                        pygame.display.flip()                            
                        pygame.time.delay(jess_no_aika) 

                        vauhti += lisataanko_vauhtia(pisteet)
                        jess_no_aika -= lisataanko_vauhtia(pisteet)
                        vaarin = False                                                  
                        oikea_nuotti.arvo_nuotti()                   
                        midi_play(oikea_nuotti.arvottu_indeksi, nykyinen_indeksi)        # MIDI täällä
                        nykyinen_indeksi = oikea_nuotti.arvottu_indeksi  
                        hirvio.nollaa()    
                        break
                    else:
                        pisteet -= 1
                        vaarin = True   
                        teksti = fontti_keski.render("NO !", True, punainen)   
                        naytto.blit(teksti, (nuotit[-1].x, nuotit[-1].y + 50))     # NO
                        naytto.blit(robotti.pic, (nuotit[-1].x , robotti.y))  
                        pygame.display.flip()                                                
                        pygame.time.delay(jess_no_aika) 
    
        
        robotti.nollaa()
        naytto.fill(tumma)
        nuottiviivasto(WIDTH - 40)  
        for nuotti in sorted(nuotit, key =lambda nuotti: nuotti.x, reverse = True ):
            if nuotti.arvottu_indeksi == 0: # keski-c:lle apuviiva
                pygame.draw.line(naytto, keltainen, (nuotti.x - 20, nuotti.y + 25), (nuotti.x + KUVAN_KOKO + 15, nuotti.y + 25), 2)

            if nuotti.y == hirvio.y:
                hirvio.korjaa_y = 0  # muutetaan hirvion liikerataa, voimaan jää pienin x, eli eka nuotti
            nuotti.liiku()
            naytto.blit(nuotti.pic, (nuotti.x , nuotti.y))   
            pelitilan_tekstit(vaarin, pisteet, nuotti)            

        for olio in oliot:
            olio.liiku()
            naytto.blit(olio.pic, (olio.x , olio.y))    
            
           
        pygame.display.flip()
        kello.tick(vauhti)
            

alkuteksti()
main()