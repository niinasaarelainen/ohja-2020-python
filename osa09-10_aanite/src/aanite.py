
class Aanite:

    def __init__(self, pituus):
        if pituus >= 0:
            self.__pituus = pituus
        else:
            raise ValueError("Pituus ei voi olla negatiivinen.")

    @property
    def pituus(self):
        return self.__pituus

    @pituus.setter
    def pituus(self, pituus):
        if pituus >= 0:
            self.__pituus = pituus
        else:
            raise ValueError("Pituus ei voi olla negatiivinen.")




if __name__ == "__main__":    
    a = Aanite(66)
    print(a.pituus)
    b = Aanite(-66)
    print(b.pituus)
    b.pituus = -77

    

