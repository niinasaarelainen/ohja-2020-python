# ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kauppalista!
# Kirjoita ratkaisusi luokan alapuolelle!
class Kauppalista:
    def __init__(self):
        self.__tuotteet = []

    def tuotteita(self):
        return len(self.__tuotteet)

    def lisaa(self, tuote: str, maara: int):
        self.__tuotteet.append((tuote, maara))

    def tuote(self, n: int):
        return self.__tuotteet[n - 1][0]

    def maara(self, n: int):
        return self.__tuotteet[n - 1][1]



def tuotteita_yhteensa(lista):
        sum = 0
        for i in range(lista.tuotteita()):
            sum += lista.maara(i)
        return sum 

if __name__ == "__main__":

    l = Kauppalista()
    l.lisaa("banaanit", 10)
    l.lisaa("omenat", 5)
    l.lisaa("ananas", 1)

    print(tuotteita_yhteensa(l))







