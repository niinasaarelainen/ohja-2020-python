from functools import reduce

class Suoritus:
    def __init__(self, kurssi: str, arvosana: int, opintopisteet: int):
        self.kurssi = kurssi
        self.arvosana = arvosana
        self.opintopisteet = opintopisteet

    def __str__(self):
        return f"{self.kurssi} ({self.opintopisteet} op) arvosana {self.arvosana}"


def kaikkien_opintopisteiden_summa(lista):
    int_lista = [suoritus.opintopisteet for suoritus in lista]
    return reduce(lambda x, y: x + y, int_lista)
    #reduce(lambda x, y: x.opintopisteet + y.opintopisteet, lista)    miksei tämä toimi !?!?

def hyvaksyttyjen_opintopisteiden_summa(lista):
    filter_lista = filter(lambda suoritus: suoritus.arvosana > 0, lista)
    int_lista = [suoritus.opintopisteet for suoritus in filter_lista if suoritus.arvosana > 0]
    return reduce(lambda x, y: x + y, int_lista) 

def keskiarvo(lista):
    filter_lista = filter(lambda suoritus: suoritus.arvosana > 0, lista)
    int_lista = [suoritus.arvosana for suoritus in filter_lista ]
    return reduce(lambda x, y: x + y, int_lista) / len(int_lista)

if __name__ == "__main__":
    s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
    s2 = Suoritus("Ohjelmoinnin jatkokutssi", 4, 0)
    s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
    summa = kaikkien_opintopisteiden_summa([s1, s2, s3])
    print("kaikkien_opintopisteiden_summa" , summa)
    
    print("hyvaksyttyjen_opintopisteiden_summa", hyvaksyttyjen_opintopisteiden_summa([s1, s2, s3]))
    
    ka = keskiarvo([s1, s2, s3])    
    print("ka",  ka)



    
