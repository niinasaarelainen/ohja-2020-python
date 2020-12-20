class Opintorekisteri:
    def __init__(self):
        self.__suoritukset = {}

    def suorituksen_lisays(self, nimi, arvosana, op):
        if nimi in self.__suoritukset:
             self.__suoritukset[nimi].korota_arvosana(arvosana)
        else:
            self.__suoritukset[nimi] = Kurssi(nimi, arvosana, op)
             
    def hae_tiedot(self, nimi):
        if nimi not in self.__suoritukset:
            return None
        else:
            return self.__suoritukset[nimi]

    def suoritukset(self):
        return self.__suoritukset

#######################################################################################
class OpintorekisteriSovellus:
    def __init__(self):
        self.__suoritukset = Opintorekisteri()   

    def ohje(self):
        print("komennot: ")        
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")

    def suorituksen_lisays(self):
        nimi = input("kurssi: ")
        arvosana = input("arvosana: ")
        op = input("opintopisteet: ")
        self.__suoritukset.suorituksen_lisays(nimi, arvosana, op)        

    def haku(self):
        nimi = input("nimi: ")
        tiedot = self.__suoritukset.hae_tiedot(nimi)
        if tiedot==None:
            print("ei suoritusta")
            return
        print(f"{tiedot.nimi()} ({tiedot.op()} op) arvosana {tiedot.arvosana()}")

    def tilastot(self):  
        data = self.__suoritukset.suoritukset()        
        op = [data[kurssi].op() for kurssi in data]
        print(f"suorituksia {len(data)} kurssilta, yhteensä {sum(op)} opintopistettä") 
        arvosanat = [data[kurssi].arvosana() for kurssi in data]  
        ka = f"{sum(arvosanat)/len(arvosanat):.1f}"
        print("keskiarvo", ka)
        print("arvosanajakauma")
        jakauma = {i: arvosanat.count(i)*"x" for i in range(1,6)}
        for rivi in jakauma:
            print(str(rivi) + ": " + str(jakauma[rivi]))
    
    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.suorituksen_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":         
                self.tilastot()
            else:
                self.ohje()

#######################################################################################
class Kurssi:

    def __init__(self, nimi, arvosana,  op):
        self.__nimi = nimi
        self.__arvosana = arvosana        
        self.__op = op

    def korota_arvosana(self, arvosana):
        if arvosana > self.__arvosana:
            self.__arvosana = arvosana

    def nimi(self):
        return self.__nimi

    def arvosana(self):
        return int(self.__arvosana)

    def op(self):
        return int(self.__op)


"""
ohpe = Kurssi("Ohpe", 5, 3)
print(ohpe)
"""


# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = OpintorekisteriSovellus()
sovellus.suorita()