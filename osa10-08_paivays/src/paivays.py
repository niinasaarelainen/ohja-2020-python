
class Paivays :
    
    def __init__(self, pv, kk, v):
        self.pv = pv
        self.kk = kk
        self.v = v

    def __eq__(self, toinen):
        if self.pv == toinen.pv and self.kk == toinen.kk and self.v == toinen.v:
            return True
        return False

    def __gt__(self, toinen):
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

    def __lt__(self, toinen):
        if self == toinen:
            return False
        return not self > toinen

    def __ne__(self, toinen):
        return not self == toinen

    def __add__(self, paivia_lisaa):
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

    def __sub__(self, toinen):
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
    print("p3 > p2", p3 > p2)

    # kasvatus:
    p3 = p1 + 3
    p5 = p1 + 30
    p6 = p1 + 90
    p4 = p2 + 400

    print(p1)
    print(p2)
    print(p3)
    print(p5)
    print("p2 + 400", p4)
    print(p6)

    # erotus:
    p1 = Paivays(4, 10, 2020)
    p2 = Paivays(2, 11, 2020)
    p3 = Paivays(28, 12, 1985)

    print(p2-p1)
    print(p1-p2)
    print(p1-p3)
