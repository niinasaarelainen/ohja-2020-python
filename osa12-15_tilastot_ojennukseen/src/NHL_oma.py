import json

class Tilasto:

    def __init__(self):
        self.tilasto = {}

    def lataa_tiedosto(self, nimi):
        with open(nimi) as tiedosto:
            data = tiedosto.read()
        self.tilasto = json.loads(data)
        print("luettiin",  len(self.tilasto), "pelaajan tiedot")             

    def hae_pelaaja(self, nimi):
        for pelaaja in self.tilasto:
            if pelaaja['name'] == nimi:
                yht = pelaaja['goals'] + pelaaja['assists']
                return f"{pelaaja['name']:<20}{pelaaja['team']:>4}{pelaaja['goals']:>4} +{pelaaja['assists']:>3} ={yht:>4}"    

    def joukkueet(self):  #2
        return sorted(list(set([pelaaja['team'] for pelaaja in self.tilasto])))

    def maat(self):   #3
        return sorted(list(set([pelaaja['nationality'] for pelaaja in self.tilasto])))

    def joukkueen_pelaajat(self, joukkue):   #4
        j_pelaajat = [pelaaja for pelaaja in self.tilasto if pelaaja['team'] == joukkue ]
        for pelaaja in sorted(j_pelaajat, key=lambda pelaaja: (-(pelaaja['goals']+ pelaaja['assists']))):
            print(self.hae_pelaaja(pelaaja['name']))

    def maan_pelaajat(self, maa):   #5
        m_pelaajat = [pelaaja for pelaaja in self.tilasto if pelaaja['nationality'] == maa ]
        for pelaaja in sorted(m_pelaajat, key=lambda pelaaja: (-(pelaaja['goals']+ pelaaja['assists']))):
            print(self.hae_pelaaja(pelaaja['name']))
            
    def eniten_pisteita(self, montako):  #6
        s = sorted(self.tilasto, key=lambda pelaaja: (-(pelaaja['goals'] + pelaaja['assists']),  -pelaaja['goals'] ))
        for pelaaja in s[:montako]:
            print(self.hae_pelaaja(pelaaja['name']))

    def eniten_maaleja(self, montako):  #7
        s = sorted(self.tilasto, key=lambda pelaaja: (-pelaaja['goals'] ,  pelaaja['games'] ))
        for pelaaja in s[:montako]:
            print(self.hae_pelaaja(pelaaja['name']))

    def vahiten_ja_eniten_rangaistuksia(self, montako):   #8   x most  __JA__ x vähiten
        s = sorted(self.tilasto, key=lambda pelaaja: -pelaaja['penalties'] )        
                
        print("eniten rangaistuksia:")
        for pelaaja in (s)[:montako]:            
             print( f"\t{pelaaja['name']:<20}{pelaaja['team']:>4}{pelaaja['penalties']:>4}")  

        print("vähiten rangaistuksia:")    
        s = sorted(self.tilasto, key=lambda pelaaja: pelaaja['penalties'] )        
        for pelaaja in s[:montako]:    
            print( f"\t{pelaaja['name']:<20}{pelaaja['team']:>4}{pelaaja['penalties']:>4}")  


######################################################################################################################
class Sovellus:

    def valikko():
        t = Tilasto()
        tiedosto = input("tiedosto: ")   
        t.lataa_tiedosto(tiedosto)     
        komennot = """
    komennot:
    0 lopeta
    1 hae pelaaja
    2 joukkueet
    3 maat
    4 joukkueen pelaajat
    5 maan pelaajat
    6 eniten pisteitä
    7 eniten maaleja
    8 vähiten ja eniten rangaistuksia
    """

        while True:            
            print(komennot)
            komento= input("komento: ")
            if komento == "0":
                break
            if komento == "1":
                nimi = input("nimi: ") 
                print(t.hae_pelaaja(nimi))
            elif komento == "2":
                for j in t.joukkueet():
                    print(j)
            elif komento == "3":
                for m in t.maat():
                    print(m)
            elif komento == "4":
                joukkue = input("joukkue: ")
                t.joukkueen_pelaajat(joukkue)    # funktio printtaa
            elif komento == "5":
                maa = input("maa: ")
                t.maan_pelaajat(maa)    # funktio printtaa
            elif komento == "6":  
                montako = int(input("kuinka monta: "))
                t.eniten_pisteita(montako)  # funktio printtaa
            elif komento == "7":  
                montako = int(input("kuinka monta: "))
                t.eniten_maaleja(montako)  # funktio printtaa
            elif komento == "8":  
                montako = int(input("kuinka monta: "))
                t.vahiten_ja_eniten_rangaistuksia(montako)  # funktio printtaa


    def test():
        t = Tilasto()
        t.lataa_tiedosto("osa.json")
        print(t.hae_pelaaja("Travis Zajac"))
        
        for j in t.joukkueet():
            print(j)

        print()
        for m in t.maat():
            print(m)

        print()
        t.joukkueen_pelaajat("OTT")

        print()
        t.maan_pelaajat("CAN")

        print()
        t.eniten_pisteita(22)

        print()
        t.eniten_maaleja(22)

        print()
        t.vahiten_ja_eniten_rangaistuksia(13)

s = Sovellus 
#s.valikko()
s.test()