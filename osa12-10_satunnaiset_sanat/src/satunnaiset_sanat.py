import random

def sanageneraattori(kirjaimet: str, pituus: int, maara: int):
    return (kirjainvalinta(pituus,kirjaimet) for i in range(maara))


def kirjainvalinta(pituus, kirjaimet):
    return "".join([random.choice(kirjaimet) for i in range(pituus)])
     

if __name__ == "__main__":
    sanagen = sanageneraattori("cdefg", 3, 5)
    for sana in sanagen:
        print(sana)



