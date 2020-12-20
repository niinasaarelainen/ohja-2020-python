import math

class Paivays :
    
    def __init__(self, pv, kk, v):
        self.pv = pv
        self.kk = kk
        self.v = v

    def __eq__(self, toinen):
        if self.pv == toinen.pv and self.kk == toinen.kk and self.v == toinen.v:
            return True
        return False

    def __gt__wanha(self, toinen):      # EI NÄIN
        if self == toinen:
            return False
        if self.v > toinen.v:
            return True
        elif self.v < toinen.v:
            return False
        # sama vuosi:
        elif self.kk > toinen.kk:
            return True
        elif self.kk < toinen.kk:
            return False
        # sama vuosi & kk:
        elif self.pv > toinen.pv:
            return True
        return False

    def muunna_paiviksi(self, pvm):                         # TODELLAKIN NÄIN
        return pvm.pv + (pvm.kk * 30) + (pvm.v * 30 * 12)

    def __gt__(self, toinen):                               # TODELLAKIN NÄIN
        pvm1 = self.muunna_paiviksi(self)
        pvm2 = self.muunna_paiviksi(toinen)
        
        return pvm2 > pvm1

    def __lt__(self, toinen):
        if self == toinen:
            return False
        return not self > toinen

    def __ne__(self, toinen):
        return not self == toinen

    def __add__(self, paivia_lisaa):    # huom! TODO p2 + 360:   28.0.1987    ei ole 0-kk
        uusi_pv = self.pv + paivia_lisaa
        uusi_kk = self.kk
        uusi_v = self.v
        if uusi_pv >30:
            uusi_kk = int(uusi_pv / 30)
            uusi_kk = uusi_kk + self.kk 
            uusi_pv = uusi_pv % 30
        if uusi_kk >12:            
            uusi_v = int(uusi_kk / 12) + self.v
            uusi_kk = uusi_kk % 12
        return Paivays(uusi_pv, uusi_kk, uusi_v)

    def __add__eitoimi(self, paivia_lisaa):   # huom! TODO p2 + 360:   28.0.1987    ei ole 0-kk
        pv1 = self.muunna_paiviksi(self)
        pv2 = pv1 + paivia_lisaa
        
        uusi_v = int(pv2 / (12 * 30))
        paivia_jaljella = pv2 - ( uusi_v*12*30)
        uusi_kk = int(paivia_jaljella / 30)        
        paivia_jaljella = paivia_jaljella - uusi_kk*30
        uusi_pv = paivia_jaljella

        if uusi_kk == 0:
            uusi_kk = 12
        return Paivays(uusi_pv, uusi_kk, uusi_v)


    def __sub__wanha(self, toinen):         # EI NÄIN
        if self > toinen:
            pvm1 = self
            pvm2 = toinen
        else:
            pvm1 = toinen
            pvm2 = self
        pv_erotus = pvm1.pv - pvm2.pv
        kk_erotus = (pvm1.kk - pvm2.kk)*30
        v_erotus = (pvm1.v - pvm2.v)*30*12        
        return pv_erotus + kk_erotus + v_erotus 

    def __sub__(self, toinen):                   #  NÄIN
        pvm1 = self.muunna_paiviksi(self)
        pvm2 = self.muunna_paiviksi(toinen)
        
        return abs(pvm1- pvm2) 

    def __repr__(self):
        return f"{self.pv}.{self.kk}.{self.v}"


if __name__ == "__main__":

    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(28, 12, 1985)
    p3 = Paivays(28, 12, 1985)

    print(p1)
    print(p2)
    print(p3)
    print("p1 == p2", p1 == p2)
    print("p3 == p2", p3 == p2)
    print("p1 == p3", p1 == p3)
    print("p1 != p2", p1 != p2)
    print("p1 < p2", p1 < p2)
    print("p2 < p3", p2 < p3)
    print("p1 > p2", p1 > p2)
    print("p2 > p1", p2 > p1)
    print("p3 > p2", p3 > p2)

    # kasvatus:
   
    print("p1 + 3", p1 + 3)
    print("p1 + 30", p1 + 30)
    print("p1 + 90", p1 + 90)
    print("p2 + 360", p2 + 360)
    print("p2 + 400", p2 + 400)
    # erotus:
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)

    print(p2-p1)
    print(p1-p2)
    print(p1-p3)
