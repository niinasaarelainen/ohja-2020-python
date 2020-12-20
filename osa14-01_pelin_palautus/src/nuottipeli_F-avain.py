import pygame, random, pygame.midi
from nuottipeli_luokat_F import *
from nuottipeli_yhteiset_F import *

def alkuteksti():
    naytto.fill(tumma)
    tekstit = []
    tekstit.append("Laita kätesi valmiiksi näppäimille f, g, a, h, c")
    tekstit.append("Aluksi kysellään vain F-vaimen matalaa f:ää ja g:tä.")
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

def midi_play(n, nykyinen_key):
    #ei voi laskea systeemillä, esim. i+=2, koska välillä on puolisävelaskel välillä koko-
    midi_numbers = {K_f: 65 -24, K_g: 67 -24, K_a: 69-24, K_h: 70 -24, K_c: 72 - 24}    # 99 = 'c',   60 = keski-c, 67 = g
    midi_out.note_off(midi_numbers[nykyinen_key])
    midi_out.note_on(midi_numbers[n], 100)
    

def lisataanko_vauhtia(pisteet):
    if pisteet % 12 == 0 and pisteet > 0:  #  0%12 == 0  
        return 22
    return 0


def pelitilan_tekstit(vaarin, pisteet, nuotti, jess_no_aika, kyselyalue):
    pisteet = fontti_iso.render(f"Pisteet: {pisteet}", True, turkoosi)
    naytto.blit(pisteet, (600, 30))    
    
    if vaarin:                         
        teksti = fontti_keski.render(f"Väärin. Nuotti on: {nuotti.nykyinen_nimi() }", True, punainen)  
        if jess_no_aika <= JESS_NO_AIKARAJA:
            jess_no = fontti_keski.render(nuotti.jess_no_teksti, True, punainen) 
            naytto.blit(jess_no, (nuotti.x, nuotti.y + 50))   
        else:
            nuotti.jess_no_teksti = "" 
            robotti.nollaa()
    else:
        teksti = fontti_keski.render(kyselyalue, True, turkoosi)       
        if jess_no_aika <= JESS_NO_AIKARAJA:
            jess_no = fontti_keski.render(nuotti.jess_no_teksti, True, turkoosi) 
            naytto.blit(jess_no, (nuotti.jess_x, nuotti.jess_y + 50))  
        else:
            nuotti.jess_no_teksti = "" 
            robotti.nollaa()
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
midi_out.set_instrument(11)   

fontti_iso = pygame.font.SysFont("Arial", 36)
fontti_keski = pygame.font.SysFont("Arial", 30)
fontti_pieni_bold = pygame.font.SysFont("Arial", 24, bold = True)

robotti = Robotti()
hirvio = Hirvio()
oliot = [robotti, hirvio]
nuotit = [Nuotti()]     # aluksi 1 nuotti, uusissa leveleissä lisää



def main():
    nuotit = [Nuotti()]      # poistetaan 2-levelin ylim.nuotit
    nollaa_kaikki()
    pisteet = 0
    vaarin = False
    vauhti = 100   # ticks
    
    jess_no_aika = 0    
    nuotit[0].arvo_nuotti()     # aluksi 1 nuotti
    nykyinen_key = 103
    kyselyalue = "F vai G?"

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
                    if tapahtuma.key in nappaimet:
                        midi_play(tapahtuma.key, nykyinen_key)          # MIDI täällä                                      
                        nykyinen_key = tapahtuma.key
                    jess_no_aika = 0

                    oikea_nuotti = None
                    oikeat_nuotit = [n for n in nuotit if chr(tapahtuma.key) == n.nykyinen_nimi()]          # voi olla useita samannimisiä näytöllä kerralla
                    if not oikeat_nuotit == []:
                        oikea_nuotti =  sorted(oikeat_nuotit, key =lambda nuotti: nuotti.x )[0]    # pienin x

                    if oikea_nuotti is not None:
                        pisteet += 1                                             # TODO 2-->20 
                        if pisteet == 3 and len(nuotit) == 1:    # miinuspist.takia voi tulla 2 pist. useasti  
                            nuotit.append(Nuotti())
                            kyselyalue = "F, G vai A?"
                            [nuotti.kasvata_ylarajaa() for nuotti in nuotit]
                        if pisteet == 6 and len(nuotit) == 2:          # TODO 5 ääntä       
                            nuotit.append(Nuotti())
                            kyselyalue = "F, G, A vai H?"
                            [nuotti.kasvata_ylarajaa() for nuotti in nuotit]
                        oikea_nuotti.jess_no_teksti = "JESS !"
                        oikea_nuotti.jess_x = oikea_nuotti.x   # pidetään teksti paikallaan, koska nuotti siirtyy heti alkuun
                        oikea_nuotti.jess_y = oikea_nuotti.y                        
                        robotti.siirry_nappaimen_maaraamaan_paikkaan(tapahtuma.key, oikea_nuotti.x)  

                        vauhti += lisataanko_vauhtia(pisteet)
                        vaarin = False                                                  
                        oikea_nuotti.arvo_nuotti()     
                        hirvio.nollaa()   
                    else:
                        pisteet -= 1
                        vaarin = True   
                        eka_nuotti = sorted(nuotit, key =lambda nuotti: nuotti.x )[0]
                        eka_nuotti.jess_no_teksti = "NO !"                               
                        robotti.siirry_nappaimen_maaraamaan_paikkaan(tapahtuma.key, eka_nuotti.x) 
            
        
        naytto.fill(tumma)
        naytto.blit(F_avain, (20 , 80)) 
        nuottiviivasto(WIDTH - 40)  

        for nuotti in sorted(nuotit, key =lambda nuotti: nuotti.x):
            nuotti.liiku()
            naytto.blit(nuotti.pic, (nuotti.x , nuotti.y))   

            if hirvio.y >= nuotti.y:
                hirvio.korjaa_y = 0  # muutetaan hirvion liikerataa, voimaan jää pienin x, eli eka nuotti

            if not nuotti.jess_no_teksti == "":
                naytto.blit(robotti.pic, (robotti.x , robotti.y))        
            
            pelitilan_tekstit(vaarin, pisteet, nuotti, jess_no_aika, kyselyalue)            

        hirvio.liiku()
        naytto.blit(hirvio.pic, (hirvio.x , hirvio.y))                
           
        pygame.display.flip()
        jess_no_aika += 1
        kello.tick(vauhti)
            

alkuteksti()
main()