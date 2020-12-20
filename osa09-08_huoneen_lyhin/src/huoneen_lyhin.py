class Henkilo:

    def __init__(self, nimi, pituus):
        self.nimi = nimi
        self.pituus = pituus

    def __repr__(self):
        return f"{self.nimi} ({self.pituus} cm)"

class Huone:

    def __init__(self):
        self.henkilot = []

    def lisaa(self, henkilo: Henkilo):
        self.henkilot.append(henkilo)

    def on_tyhja(self):
        return self.henkilot == []

    def tulosta_tiedot(self):
        summa = sum([h.pituus for h in self.henkilot])
        print(f"Huoneessa {len(self.henkilot)} henkilöä, yhteispituus {summa} cm")
        for h in self.henkilot:
            print(h)

    def lyhin(self):
        s = sorted([(h.pituus, h) for h in self.henkilot])
        if self.henkilot == []:
            return None
        print(s)
        return s[0][1]    # koko henkilo

    def lyhin2(self):        
        if self.henkilot == []:
            return None
        s = sorted(self.henkilot, key=lambda h: h.pituus)
        print(s)
        return s[0].nimi   # vain nimi


    def poista_lyhin(self):
        if self.henkilot == []:
            return None
        s = sorted([(h.pituus, h) for h in self.henkilot])        
        lyhin = s[0][1]  
        self.henkilot.remove(s[0][1])      
        return lyhin

    def poista_lyhin2(self):
        if self.henkilot == []:
            return None
        s = sorted(self.henkilot, key=lambda h: h.pituus)
        lyhin = s[0]
        self.henkilot.remove(lyhin)      
        return lyhin



if __name__ == "__main__":
    huone = Huone()
    print("Lyhin: ", huone.lyhin())

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Auli", 186))
    huone.lisaa(Henkilo("Nina", 172))

    huone.tulosta_tiedot()
    print()
    print("Lyhin: ", huone.lyhin())
    print("Lyhin2: ", huone.lyhin2())

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta: {poistettu.nimi}")

    print()
    huone.tulosta_tiedot()

    poistettu = huone.poista_lyhin2()
    print(f"Otettiin huoneesta: {poistettu.nimi}")

    print()
    huone.tulosta_tiedot()