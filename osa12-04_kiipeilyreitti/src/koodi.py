class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"

def vaikeuden_mukaan(reitit: list):
    return sorted(pituuden_mukaan(reitit), key=lambda alkio: alkio.grade, reverse = True)     


def pituuden_mukaan(reitit: list):
    return sorted(reitit, key=lambda alkio: alkio.pituus, reverse = True)     


if __name__ == "__main__":
    r1 = Kiipeilyreitti("Kantti", 38, "6A+")
    r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
    r3 = Kiipeilyreitti("Syncro", 14, "8C+")
    r4 = Kiipeilyreitti("Suuri leikkaus", 36, "6B")
    r5 = Kiipeilyreitti("Hedelmätarha", 8, "6A")
    r6 = Kiipeilyreitti("Possu ei pidä", 12 , "6B+")
    r7 = Kiipeilyreitti("Pieniä askelia", 13, "6A+")
    r8 = Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+")
    vastaus = vaikeuden_mukaan([r1, r2, r3, r4, r5, r6, r7, r8])
    #vastaus = pituuden_mukaan([r1, r2, r3, r4, r5, r6, r7, r8])

    for reitti in vastaus:
        print(reitti)
