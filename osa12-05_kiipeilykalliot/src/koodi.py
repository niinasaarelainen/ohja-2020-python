class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"

class Kiipeilykallio:
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.__reitit = []

    def lisaa_reitti(self, reitti: Kiipeilyreitti):
        self.__reitit.append(reitti)

    def reitteja(self):
        return len(self.__reitit)

    def vaikein_reitti(self):
        def vaikeuden_mukaan(reitti):
            return reitti.grade
        return sorted(self.__reitit, key=vaikeuden_mukaan)[-1]

    def __str__(self):
        return f"{self.nimi} {self.reitteja()} reittiä, vaikein {self.vaikein_reitti().grade}"


def reittien_maaran_mukaan(kalliot:list):
    return sorted(kalliot, key=lambda kallio: kallio.reitteja())   



def vaikeimman_reitin_mukaan(kalliot:list):
    #return list(reversed(vaikeuden_mukaan[kallio for kallio.vaikein_reitti() in kalliot])
    return sorted(kalliot, key=lambda kallio: kallio.vaikein_reitti().grade, reverse = True)   


 

if __name__ == "__main__":

    k1 = Kiipeilykallio("Olhava")
    k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
    k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
    k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

    k2 = Kiipeilykallio("Nummi")
    k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))

    k3 = Kiipeilykallio("Nalkkilan släbi")
    k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))
    k3.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A"))
    k3.lisaa_reitti(Kiipeilyreitti("Possu ei pidä", 12 , "6B+"))
    k3.lisaa_reitti(Kiipeilyreitti("Hedelmätarha", 8, "6A"))
    print("vaikein_reitti:", k3.vaikein_reitti())

    print(k1)
    print(k3.nimi, k3.reitteja())
    print(k3.vaikein_reitti())
    kalliot = [k1, k2, k3]
    print()
    for kallio in reittien_maaran_mukaan(kalliot):
        print(kallio)

    print()
    for kallio in vaikeimman_reitin_mukaan(kalliot):
        print(kallio)