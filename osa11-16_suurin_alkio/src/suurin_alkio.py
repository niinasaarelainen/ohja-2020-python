# TEE RATKAISUSI TÄHÄN:
class Alkio:
    """ Luokka mallintaa yhtä alkiota binääripuussa """
    def __init__(self, arvo, vasen_lapsi:'Alkio' = None, oikea_lapsi:'Alkio' = None):
        self.arvo = arvo
        self.vasen_lapsi = vasen_lapsi
        self.oikea_lapsi = oikea_lapsi

def suurin_alkio(juuri: Alkio):
    suurin = juuri.arvo

    if juuri.vasen_lapsi is not None:
        suurin = max(suurin, suurin_alkio(juuri.vasen_lapsi))
        print("suurin_v", suurin)

    if juuri.oikea_lapsi is not None:
        suurin = max(suurin, suurin_alkio(juuri.oikea_lapsi))
        print("suurin_o", suurin)

    return suurin


if __name__ == "__main__":
    puu = Alkio(2)

    puu.vasen_lapsi = Alkio(33)
    puu.vasen_lapsi.vasen_lapsi = Alkio(12)
    puu.vasen_lapsi.oikea_lapsi = Alkio(13)

    puu.oikea_lapsi = Alkio(11)
    puu.oikea_lapsi.oikea_lapsi = Alkio(31)
    puu.oikea_lapsi.oikea_lapsi.oikea_lapsi= Alkio(14)

    print(suurin_alkio(puu))

    puu2 = Alkio(13)

    puu2.vasen_lapsi = Alkio(15)
    puu2.vasen_lapsi.vasen_lapsi = Alkio(17)
    puu2.vasen_lapsi.oikea_lapsi = Alkio(24)

    puu2.oikea_lapsi = Alkio(14)
    puu2.oikea_lapsi.oikea_lapsi = Alkio(9)
    puu2.oikea_lapsi.oikea_lapsi.oikea_lapsi= Alkio(8)
    puu2.oikea_lapsi.oikea_lapsi.vasen_lapsi= Alkio(29)

    print(suurin_alkio(puu2))