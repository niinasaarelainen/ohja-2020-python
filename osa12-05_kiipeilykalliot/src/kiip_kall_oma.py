from functools import reduce    # "flatten":ia varten

class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade
        self.onko_kiivetty = False

    def __gt__(self, verrokki):
        return self.nimi > verrokki.nimi

    def tikkaa(self):
        self.onko_kiivetty = True

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

    def reitit_graden_mukaan(self, grade):
        reitit = [(self.nimi, reitti) for reitti in self.__reitit if reitti.grade== grade]        
        return reitit

    def kiivetyt(self):
        return [(self.nimi, reitti) for reitti in self.__reitit if reitti.onko_kiivetty== True]        
         

    def vaikein_reitti(self):
        def vaikeuden_mukaan(reitti):
            return reitti.grade
        return sorted(self.__reitit, key=vaikeuden_mukaan)[-1]

    def __str__(self):
        return f"{self.nimi} {self.reitteja()} reittiä, vaikein {self.vaikein_reitti().grade}"

# !!!
def etsi_tietyn_greidin_reitit(kalliot:list, grade):
    # tähän tulee yhdet sulkuparit liikaa
    #astaus_lista = [kallio.reitit_graden_mukaan(grade) for kallio in kalliot if kallio.reitit_graden_mukaan(grade) != []]
    
    for kallio in kalliot:        
        vastaus_lista = kallio.reitit_graden_mukaan(grade)
        for kallion_nimi, reitti in vastaus_lista:
           print(kallion_nimi, ": " ,  reitti)
           
    #return sorted(kalliot, key=lambda kallio: kallio.reitit_graden_mukaan(grade))   
    # tämä ei sovelias, koska ei haluata palauttaa kaikkia kallioita: ei välttis ole tiettyä greidiä

def kiivetyt_greidin_mukaan(kalliot:list):
    vastaus_lista = []
    for kallio in kalliot:        
        vastaus_lista.append(kallio.kiivetyt())
    vastaus_lista = reduce(lambda x,y: x+y,vastaus_lista)    # flatten = [1,2,3],[4,5,6], [7] --> [1, 2, 3, 4, 5, 6, 7]
    return sorted(vastaus_lista, key=lambda kallio: kallio[1].grade)   

def reittien_maaran_mukaan(kalliot:list):
    return sorted(kalliot, key=lambda kallio: kallio.reitteja())   

def vaikeimman_reitin_mukaan(kalliot:list):
    #return list(reversed(vaikeuden_mukaan[kallio for kallio.vaikein_reitti() in kalliot])
    return sorted(kalliot, key=lambda kallio: kallio.vaikein_reitti().grade, reverse = True)   



 

if __name__ == "__main__":

    k1 = Kiipeilykallio("Olhava")
    kantti = Kiipeilyreitti("Kantti", 38, "6A+")
    k1.lisaa_reitti(kantti)
    kantti.tikkaa()
    k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
    k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))


    k2 = Kiipeilykallio("Nummi")
    k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))

    k3 = Kiipeilykallio("Nalkkilan släbi")
    k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))
    k3.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A"))
    possu = Kiipeilyreitti("Possu ei pidä", 12 , "6B+")
    k3.lisaa_reitti(possu)
    possu.tikkaa()
    hedelma = Kiipeilyreitti("Hedelmätarha", 8, "6A")
    k3.lisaa_reitti(hedelma)
    hedelma.tikkaa()
    k3.lisaa_reitti(Kiipeilyreitti("Niinan erikoinen", 28, "6A+"))
    
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

    print("\netsi_tietyn_greidin_reitit:")
    etsi_tietyn_greidin_reitit(kalliot, "6A+")

    print("\nkiivetyt:")    
    for kallion_nimi, reitti in kiivetyt_greidin_mukaan(kalliot):
        print(kallion_nimi, ": " ,  reitti)
       