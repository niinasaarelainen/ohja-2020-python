
class Palloilija:
    def __init__(self, nimi: str, pelinumero: int, maalit: int, syotot: int, minuutit: int):
        self.nimi = nimi
        self.pelinumero = pelinumero
        self.maalit = maalit
        self.syotot = syotot
        self.minuutit = minuutit

    def __repr__(self):
        return (f'Palloilija(nimi={self.nimi}, pelinumero={self.pelinumero}, ' 
            f'maalit={self.maalit}, syotot={self.syotot}, minuutit={self.minuutit})')


def eniten_maaleja(palloilijat):
    return max(palloilijat, key=lambda palloilija: palloilija.maalit).nimi

def eniten_pisteita(palloilijat):
        p = max(palloilijat, key=lambda palloilija: palloilija.maalit + palloilija.syotot)
        return (p.nimi, p.pelinumero)

def vahiten_minuutteja(palloilijat):
    return min(palloilijat, key=lambda palloilija: palloilija.minuutit)


if __name__ == "__main__":
    # eniten maaleja: Kimmo
    palloilijat = [Palloilija("Pekka",4,1,6,900), Palloilija("Armas",6,4,3,885), Palloilija("Jarppi",9,9,2,840), Palloilija("Kimmo", 3,13,9,1034)]
    for i in range(4000):
        print(eniten_maaleja(palloilijat))
    