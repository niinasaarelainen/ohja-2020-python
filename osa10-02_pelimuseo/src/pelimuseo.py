# TEE RATKAISUSI TÄHÄN:
class Tietokonepeli:
    def __init__(self, nimi: str, julkaisija: str, vuosi: int):
        self.nimi = nimi
        self.julkaisija = julkaisija
        self.vuosi = vuosi


class Pelivarasto:

    def __init__(self):
        self.__pelit = []

    def lisaa_peli(self, peli: Tietokonepeli):
        self.__pelit.append(peli)

    def anna_pelit(self):
        return self.__pelit


class Pelimuseo(Pelivarasto):

    def __init__(self):
        super().__init__()

    def anna_pelit(self):
        uudet_pelit = []
        for peli in super().anna_pelit():   # huom! ei voi olla pelkkä anna_pelit()
        # for peli in Pelivarasto.anna_pelit(self):    tämä kävisi myös
            if peli.vuosi < 1990:
                uudet_pelit.append(peli)
        return uudet_pelit

#######################################################################################################
if __name__ == "__main__":
    museo = Pelimuseo()
    museo.lisaa_peli(Tietokonepeli("Pacman", "Namco", 1980))
    museo.lisaa_peli(Tietokonepeli("GTA 2", "Rockstar", 1999))
    museo.lisaa_peli(Tietokonepeli("Bubble Bobble", "Taito", 1986))
    for peli in museo.anna_pelit():
        print(peli.nimi)