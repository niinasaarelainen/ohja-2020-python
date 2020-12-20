
import random

class Tyontekija:
    def __init__(self, nimi: str, palkka = 4400):
        self.nimi = nimi
        self.palkka = palkka
        self.alaiset = []

    def lisaa_alainen(self, tyontekija: 'Tyontekija'):
        self.alaiset.append(tyontekija)

    def __str__(self):
        return self.nimi

class TyontekijaPomoTiedossa:
    def __init__(self, nimi: str, pomo):
        self.nimi = nimi
        self.alaiset = []
        self.pomo = pomo.nimi

    def lisaa_alainen(self, tyontekija: 'Tyontekija'):
        self.alaiset.append(tyontekija)

    def __str__(self):
        return self.nimi +" (pomo: " + self.pomo +")"



def laske_alaiset(tyontekija: Tyontekija):    
    summa = len(tyontekija.alaiset)
    for alainen in tyontekija.alaiset:
        if tyontekija.alaiset != []:  
            print(alainen)
        summa +=  laske_alaiset(alainen) 

    return summa

def alaisten_nimet_listaan(tyontekija: Tyontekija, nimet):   # lista parametrina
    nimet.append((tyontekija.nimi, tyontekija.palkka))
    for alainen in tyontekija.alaiset:
        alaisten_nimet_listaan(alainen, nimet) 

    return sorted(nimet[1:])  # ekana on pomo, se pois heti

def alaiset_palkan_mukaan(tyontekija: Tyontekija, nimet):   # lista parametrina
    nimet.append((tyontekija.nimi, tyontekija.palkka))
    for alainen in tyontekija.alaiset:
        alaisten_nimet_listaan(alainen, nimet) 

    #                                   huom! tämä    ja  tämä  pitää olla samannimiset
    return sorted(nimet[1:], key=lambda nimi_ja_palkka: nimi_ja_palkka[1], reverse = True)  # ekana on pomo, se pois heti


#ei toimi, tulee vain pomo
def alaisten_nimet_listaan2(tyontekija: Tyontekija):   # lista __EI__ parametrina    
   return [alainen.nimi if alaisten_nimet_listaan2(alainen) else alaisten_nimet_listaan2(alainen) for alainen in tyontekija.alaiset ]
     
        




if __name__ == "__main__":
    t1 = Tyontekija("Sasu")
    t2 = Tyontekija("Erkki", 6600)
    t3 = Tyontekija("Matti")
    t4 = Tyontekija("Emilia", 5500)
    t5 = Tyontekija("Antti")
    t6 = Tyontekija("Kjell")
    
    t1.lisaa_alainen(t6)    # "Kjell"
    t1.lisaa_alainen(t4)   # "Emilia"
    t4.lisaa_alainen(t2)    # "Erkki"
    t4.lisaa_alainen(t3)   # "Matti"
    t4.lisaa_alainen(t5)

    t3.lisaa_alainen(Tyontekija("Alaisen alaisen alainen"))   # Matin, Emilian ja Sasun alainen

    print("\nt1:")
    print(laske_alaiset(t1))   #6
    print("\nt4:")
    print(laske_alaiset(t4))   #4
    print("\nt5:")
    print(laske_alaiset(t5))   #0

    lista = alaisten_nimet_listaan(t1, [])   # lista  parametrina
    print(lista)
    lista = alaisten_nimet_listaan(t4, [])
    print(lista)
    lista = alaisten_nimet_listaan(t5, [])
    print(lista)

    lista = alaisten_nimet_listaan2(t1)  # lista __EI__ parametrina
    print(lista)
    lista = alaisten_nimet_listaan2(t4)
    print(lista)
    lista = alaisten_nimet_listaan2(t5)
    print(lista)

    lista = alaiset_palkan_mukaan(t1, [])   # lista  parametrina
    print(lista)
    lista = alaiset_palkan_mukaan(t4, [])
    print(lista)
    lista = alaiset_palkan_mukaan(t5, [])
    print(lista)

    def muodosta_alaisen_nimi():
        konsonantit = "wrtplkjhgfdszxvbnm"
        runko = "iiviaavi"
        konsonantti = random.choice(konsonantit)       
        return konsonantti + runko[:4] + konsonantti +  runko[4:]

    
    
    
    t1 = Tyontekija("Ylin pomo")
    for i in range(4):
        t1.lisaa_alainen(TyontekijaPomoTiedossa(muodosta_alaisen_nimi(), t1))

    for i in range(2):
        for alainen in t1.alaiset:
            alainen.lisaa_alainen(TyontekijaPomoTiedossa(muodosta_alaisen_nimi(), alainen))

    print(laske_alaiset(t1))   # täällä myös print

        
    