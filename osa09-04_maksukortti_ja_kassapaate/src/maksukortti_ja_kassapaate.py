class Maksukortti:

    def __init__(self, saldo: float):
        self.saldo = saldo

    def lataa_rahaa(self, lisays: float):
        self.saldo += lisays    

    def ota_rahaa(self, maara: float):
        if self.saldo >= maara:
            self.saldo -= maara
            return True
        else:
            return False

   
class Kassapaate:

    maukkaan_hinta = 4.3
    edullisen_hinta = 2.5
    
    def __init__(self):
        self.rahaa = 1000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti(self, maksu: float):        
        if maksu >= self.edullisen_hinta:
            self.edulliset += 1
            self.rahaa += self.edullisen_hinta
            return maksu - self.edullisen_hinta
        else:
            return float(maksu)

    def syo_maukkaasti(self, maksu: float):        
        if maksu >= 4.3:
            self.maukkaat += 1
            self.rahaa += self.maukkaan_hinta
            return maksu - self.maukkaan_hinta
        else:
            return float(maksu)

    def syo_edullisesti_kortilla(self, kortti:Maksukortti):
        if kortti.saldo >= self.edullisen_hinta:
            kortti.saldo -= self.edullisen_hinta
            self.edulliset += 1
            return True
        else:
            return False

    def syo_maukkaasti_kortilla(self, kortti:Maksukortti):
        if kortti.saldo >= self.maukkaan_hinta:
            kortti.saldo -= self.maukkaan_hinta
            self.maukkaat += 1
            return True
        else:
            return False

    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa:float ):
        self.rahaa += summa
        kortti.lataa_rahaa(summa) 

        
    def __repr__(self):
        return f"kassassa rahaa {self.rahaa} edullisia lounaita myyty {self.edulliset} maukkaita lounaita myyty {self.maukkaat}"



if __name__ == "__main__":

    unicafe_exactum = Kassapaate()
    print(unicafe_exactum)

    antin_kortti = Maksukortti(2)

    print(f"kortilla rahaa {antin_kortti.saldo} euroa")

    onnistuiko = unicafe_exactum.syo_maukkaasti_kortilla(antin_kortti)
    print("riittikö raha:", onnistuiko)

    unicafe_exactum.lataa_rahaa_kortille(antin_kortti, 100)

    onnistuiko = unicafe_exactum.syo_maukkaasti_kortilla(antin_kortti)
    print("riittikö raha:", onnistuiko)

    print(f"kortilla rahaa {antin_kortti.saldo} euroa")

    print(unicafe_exactum)