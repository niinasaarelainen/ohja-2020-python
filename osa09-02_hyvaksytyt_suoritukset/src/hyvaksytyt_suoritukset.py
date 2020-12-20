# Tee ratkaisusi luokan Koesuoritus perään.
# ÄLÄ MUUTA LUOKKAA
class Koesuoritus:
    def __init__(self, suorittaja: str, pisteet: int):
        self.suorittaja = suorittaja
        self.pisteet = pisteet
    def __repr__(self):
        return f'Koesuoritus (suorittaja: {self.suorittaja}, pisteet: {self.pisteet})'

# TEE RATKAISUSI TÄHÄN:

def hyvaksytyt(suoritukset: list, pisteraja: int):
    hyvaksutut = []
    for suoritus in suoritukset:
        if suoritus.pisteet >= pisteraja:
            hyvaksutut.append(suoritus)
    return hyvaksutut









