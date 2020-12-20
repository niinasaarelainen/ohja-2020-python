class ListaApuri:

    @classmethod
    def suurin_frekvenssi(cls, lista: list):
        frek = {}
        for i in lista:
            frek[lista.count(i)] = i
        if frek == {}:
            return "lista oli tyhjä"
        return frek[max(frek)]

    @classmethod
    def tuplia(cls, lista: list):
        tulos = 0
        for i in set(lista):
            montako = lista.count(i)
            if montako >= 2:
                tulos += 1
        return tulos



if __name__ == "__main__":
    luvut = [1,1,2,1,3,3,4,5,5,5,6,5,5,5]
    print(ListaApuri.suurin_frekvenssi(luvut))
    print(ListaApuri.tuplia(luvut))

    luvut2 = [9, 8, 7, 9, 8, 6, 6, 5, 5, 4, 3, 3]
    print(ListaApuri.suurin_frekvenssi(luvut2))
    print(ListaApuri.tuplia(luvut2))

    luvut3 = []
    print(ListaApuri.suurin_frekvenssi(luvut3))
    print(ListaApuri.tuplia(luvut3))