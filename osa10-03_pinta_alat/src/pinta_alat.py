
class Suorakulmio:
    def __init__(self, leveys: int, korkeus: int):
        self.leveys = leveys
        self.korkeus = korkeus
 
    def __str__(self):
        return f"suorakulmio {self.leveys}x{self.korkeus}"
 
    def pinta_ala(self):
        return self.leveys * self.korkeus

class Nelio(Suorakulmio):
    
    def __init__(self, s):
        super().__init__(s, s)

    def __str__(self):
        return f"neliö {self.leveys}x{self.korkeus}"


class SuorakulmainenKolmio(Suorakulmio):  # ei tartte __init__ jos ja kun sama
                                          # kuin perityssä luokassa

    def pinta_ala(self):
        return super().pinta_ala() / 2
        
    def __str__(self):
        return f"suorakulmainen kolmio {self.leveys}x{self.korkeus}"


#if __name__ == "__main__":
