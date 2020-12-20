class Lottorivi:

    def __init__(self, kierros_nro, numerot):
        self.kierros_nro = kierros_nro
        self.numerot = numerot

    def osumien_maara(self, pelattu_rivi: list):
        return len([nro for nro in pelattu_rivi if nro in self.numerot])

    def osumat_paikoillaan(self, pelattu_rivi):
        return [nro if nro in self.numerot else -1 for nro in pelattu_rivi]




if __name__ == "__main__":
    oikea = Lottorivi(2, [1,2,3,4,5,6,7])
    oma_rivi = [1,4,7,11,13,19,24]

    print(oikea.osumien_maara(oma_rivi))

    oikea = Lottorivi(1, [1,2,3,10,20,30,33])
    oma_rivi = [1,4,7,10,11,20,30]

    print(oikea.osumat_paikoillaan(oma_rivi))  # [1, -1, -1, 10, -1, 20, 30]