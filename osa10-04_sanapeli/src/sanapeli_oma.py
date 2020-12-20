import random

class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)
    def pelaa(self):
        for i in range(1, self.kierrokset+1):
            print(f"\nkierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            winner, ohje = self.kierroksen_voittaja(vastaus1, vastaus2)
            if  winner == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif winner == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            else:
                print("tasapeli")

            print(ohje)

        print("\npeli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")




class PisinSana(Sanapeli):    

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1
        elif len(pelaaja1_sana) < len(pelaaja2_sana):
            return 2
        return -1 # tasapeli

    
class EnitenVokaaleja(Sanapeli):
    
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # ilman settiä laskettaisiin sanan moro o:t 2 kertaa
        p1 = sum([pelaaja1_sana.count(kirjain)  for kirjain in set(pelaaja1_sana) if kirjain in "aeiouyäöå"])
        p2 = sum([pelaaja2_sana.count(kirjain)  for kirjain in set(pelaaja2_sana) if kirjain in "aeiouyäöå"])
      
        if p1 > p2:
            return 1
        elif p1 < p2:
            return 2
        return -1 # tasapeli


class KiviPaperiSakset(Sanapeli):

     def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
         sanakirja = {"kivi":1,  "paperi":2,  "sakset":4}
         if pelaaja1_sana not in sanakirja:
             if pelaaja2_sana not in sanakirja:
                 return -1
             else:
                 return 2
         if pelaaja2_sana not in sanakirja:
            return 1
         if sanakirja[pelaaja1_sana] == sanakirja[pelaaja2_sana] :
             return -1
         if sanakirja[pelaaja1_sana] - sanakirja[pelaaja2_sana] in [-3, 1, 2]:
             return 1
         return 2


class Osasanat(Sanapeli):   # kuten ei saa sanoa samaa sanaa kahdesti

    def __init__(self, kierrokset: int, sana):
        super().__init__(kierrokset)
        self.sana = sana
        self.kaytetyt_sanat = []
        print(self.ohje())
        
    def ohje(self):
        return f"\nKeksi uusia sanoja sanasta {self.sana}"

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):        

        
        ok_pelaaja1 = self.ok(pelaaja1_sana)
        ok_pelaaja2 = self.ok(pelaaja2_sana)              

        if (ok_pelaaja1 and ok_pelaaja2) or (not ok_pelaaja1 and not ok_pelaaja2):
            return -1, self.ohje()  # tasapeli

        if ok_pelaaja1:            
            return 1, self.ohje()
        return 2, self.ohje()
       

    def ok(self, s):
        if s == "" or s in self.kaytetyt_sanat:
            return False

        lista = list(self.sana)
        for kirjain in s:
            if kirjain in lista:
                lista.remove(kirjain)    # ei saa sijoittaa lista = lista.remove(kirjain)
            else:
                return False

        self.kaytetyt_sanat.append(s)
        return True

if __name__ == "__main__":
    #p = PisinSana(3)
    #p.pelaa()

    #p = KiviPaperiSakset(3)
    #p.pelaa()
    
    p = Osasanat(7, "luukkainen")    
    p.pelaa()