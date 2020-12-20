class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta: int, kuvaus):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta
        self.kuvaus = kuvaus


def halvemmat(asunnot: list, verrattava: Asunto):
    return [(asunto, verrattava.neliohinta*verrattava.nelioita - asunto.neliohinta*asunto.nelioita) for asunto in asunnot if asunto.neliohinta*asunto.nelioita < verrattava.neliohinta*verrattava.nelioita]



if __name__ == "__main__":
    a1 = Asunto(1, 16, 5500, "Eira yksiö")
    a2 = Asunto(2, 38, 4200, "Kallio kaksio")
    a3 = Asunto(3, 78, 2500, "Jakomäki kolmio")
    a4 = Asunto(6, 215, 500, "Suomussalmi omakotitalo")
    a5 = Asunto(4, 105, 1700, "Kerava 4h ja keittiö")
    a6 = Asunto(25, 1200, 2500, "Haikon kartano")

    asunnot = [a1, a2, a3, a4, a5, a6]

    print(f"asuntoa {a3.kuvaus} halvemmat vaihtoehdot:")
    for alkio in halvemmat(asunnot, a3):
        print(f"{alkio[0].kuvaus:30} hintaero {alkio[1]} euroa")