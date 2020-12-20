class Lemmikki:

    def __init__(self, nimi: str, laji: str, vuosi: int):
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = vuosi

    


def uusi_lemmikki(nimi: str, laji: str, vuosi: int):
        return Lemmikki(nimi, laji, vuosi)
        

if __name__ == "__main__":
    musti = uusi_lemmikki("Musti", "koira", 2017) 
    print(musti.nimi)
    print(musti.laji)
    print(musti.syntymavuosi)