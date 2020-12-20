# ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kirja
# Kirjoita ratkaisui Kirja-luokan jälkeen

class Kirja:
    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre 
        self.kirjoitusvuosi = kirjoitusvuosi

    # Tämä mahdollistaa kirjaolion järkevän tulostamisen print-funktiolla
    def __repr__(self):
        return f"{self.nimi} ({self.kirjoittaja}), {self.kirjoitusvuosi} - genre: {self.genre}"



def genren_kirjat(kirjat: list, genre: str):
    return sorted([kirja  for kirja in kirjat if kirja.genre == genre], key=lambda kirja: kirja.nimi[-1])

def kirjoittajan_vuosi(kirjat: list, kirjailija: str):
    return sorted([kirja.kirjoitusvuosi  for kirja in kirjat if kirja.kirjoittaja == kirjailija], reverse = True)


python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
surma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)
norma = Kirja("Surma", "Sofi Oksanen", "rikos", 2017)

kirjat = [python, everest, norma, surma, Kirja("Lumiukko", "Jo Nesbø", "rikos", 2007)]

print("rikoskirjoja ovat")
for kirja in genren_kirjat(kirjat, "rikos"):
    print(f"{kirja.kirjoittaja}: {kirja.nimi}")

print("Sofi Oksanen kirjoittanut vuosina:")
for v in kirjoittajan_vuosi(kirjat, "Sofi Oksanen"):
    print(v)