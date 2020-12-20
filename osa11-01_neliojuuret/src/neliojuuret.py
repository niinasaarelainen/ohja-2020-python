
from math import sqrt


def apufunktio(luvut):
    l = []
    for luku in luvut:
        l.append(sqrt(luku))
    return l

#huijausyritys:
def neliojuuret(luvut: list):
    return [apufunktio(luvut)]


if __name__ == "__main__":
    rivit = neliojuuret([1,2,3,4])
    for rivi in rivit:
        print(rivi)

    """
    # oikea ratkaisu
    def neliojuuret(luvut: list):
        return [sqrt(luku) for luku in luvut]
    """
