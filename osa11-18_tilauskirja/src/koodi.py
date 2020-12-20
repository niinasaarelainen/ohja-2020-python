class Tehtava:

    id = 1

    def __init__(self, kuvaus, koodari, tyomaara):        
        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = tyomaara
        self.valmis = False
        self.id = Tehtava.id
        Tehtava.id += 1 
       

    def on_valmis(self):
        return self.valmis

    def merkkaa_valmiiksi(self):
        self.valmis = True

    def valmisko(self):
        if self.valmis:
            return "VALMIS"
        return "EI VALMIS"


    def __str__(self):
        return f"{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} {self.valmisko()}"

class Tilauskirja:

    def __init__(self):
        self.__tilaukset = []

    def lisaa_tilaus(self, kuvaus, koodari, tyomaara):
        t = Tehtava(kuvaus, koodari, tyomaara)
        self.__tilaukset.append(t)

    def kaikki_tilauset(self):    # korjaa takaisin
        return self.__tilaukset

    def koodarit(self):
        return list(set([t.koodari for t in self.__tilaukset]))

    
    def merkkaa_valmiiksi(self, id: int):        
        loytyi = False
        for t in self.__tilaukset:
            if t.id == id:
                loytyi = True
                tilaus = t
        if loytyi:
            tilaus.merkkaa_valmiiksi()
        else:
            raise ValueError("Tätä id:tä ei ole olemassa") 

    def valmiit_tilauset(self): # korjaa takaisin
        return [t for t in self.__tilaukset if t.valmis] 

    def ei_valmiit_tilauset(self): # korjaa takaisin
        return [t for t in self.__tilaukset if t.valmis== False] 

    def koodarin_status(self, koodari: str):
        if len([t for t in self.__tilaukset if t.koodari == koodari]) != 0:
            valmistuneiden_maara = len([t for t in self.__tilaukset if t.valmis and t.koodari == koodari])
            valmistumattomien_maara =  len([t for t in self.__tilaukset if not t.valmis and t.koodari == koodari])
            valmistuneiden_h =  sum([t.tyomaara for t in self.__tilaukset if t.valmis and t.koodari == koodari])
            valmistumattomien_h = sum([t.tyomaara for t in self.__tilaukset if not t.valmis and t.koodari == koodari])
        else:
            raise ValueError ("ei ole tälläinen koodari täällä töissä")
        return (valmistuneiden_maara, valmistumattomien_maara, valmistuneiden_h, valmistumattomien_h)


if __name__ == "__main__":
    tilaukset = Tilauskirja()
    tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Antti", 25)
    tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)
    tilaukset.lisaa_tilaus("tee uusi facebook", "Erkki", 1000)

    tilaukset.merkkaa_valmiiksi(1)
    tilaukset.merkkaa_valmiiksi(2)

    status = tilaukset.koodarin_status("Antti")
    print(status)

    
