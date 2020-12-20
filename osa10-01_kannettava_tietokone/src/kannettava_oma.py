# TEE RATKAISUSI TÄHÄN:
class Tietokone:

    id = 0

    def __init__(self, malli: str, nopeus: int):
        self.__malli = malli
        self.__nopeus = nopeus
        Tietokone.id += 1

    @property
    def malli(self):
        return self.__malli

    @property
    def nopeus(self):
        return self.__nopeus

    def kerro_id(self):
        return Tietokone.id     #self.id

    def __str__(self):
        return f"{self.malli}, {self.nopeus} MHz"


class KannettavaTietokone(Tietokone):

    id = 0    # huom! tämä ei vaikuta, vaan yläluokasta jatkuu id:n jatkuva numerointi

    def __init__(self,  malli: str, nopeus: int, paino:int):
        super().__init__(malli, nopeus)
        self.__paino = paino
        KannettavaTietokone.id += 1

    def kerro_id(self):
        return KannettavaTietokone.id     #self.id

    def __str__(self):
        return f"{self.malli}, {self.nopeus} MHz, {self.__paino} kg"


class Padi(KannettavaTietokone):

    def lisaa_mitat(self, x, y):     # huom!! def __init__ ei tarvita, periytyy kokonaan Kannettavasta
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.malli}, {self.nopeus} MHz, {self.x} x {self.y} cm"   # huom! tämä toimii, __paino EI !!!
        #return f"{self.malli}, {self.nopeus} MHz, {self.__paino} kg"



if __name__ == "__main__":
    tk1 = Tietokone("Tietokone1", 1520)
    print(tk1.kerro_id())
    print(tk1)

    tk2 = Tietokone("Tietokone2", 1520)
    print(tk2.kerro_id())
    print(tk2)
    
    ipm = KannettavaTietokone("IPM MikroMauri", 1500, 2)
    print(ipm.kerro_id())
    print(ipm)

    ipm2 = KannettavaTietokone("IPM Sika", 2500, 2)
    print("ipm2", ipm2.kerro_id())
    print(ipm2)

    ipm3 = KannettavaTietokone("IPM Sika", 3500, 2)
    print("ipm3", ipm3.kerro_id())   #3
    print(ipm3)

    padi = Padi("Joku Padi", 500, 0.3)
    padi.lisaa_mitat(20, 17)
    print("padi", padi.kerro_id())   #4

    print(padi)