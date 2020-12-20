def hae(tuotteet: list, kriteeri: callable):
    return [tuote for tuote in tuotteet if kriteeri(tuote)]


if __name__ == "__main__":
    tuotteet = [("banaani", 5.95, 12), ("omena", 3.95, 3), ("appelsiini", 4.50, 2), ("vesimeloni", 4.95, 22), ("Kaali", 0.99, 1)]
    
    tuotteet2 = [("banaani", "keltainen"), ("omena", "vihreä"), ("appelsiini", "keltainen"), ("vesimeloni", "punainen")]


    def hinta_alle_4_euroa(tuote):
        return tuote[1] < 4

    def hinta_yli_4_euroa(tuote):
        return tuote[1] > 4

    def keltainenko(tuote):
        return tuote[1] == "keltainen"


    for tuote in hae(tuotteet, hinta_alle_4_euroa):
        print(tuote)

    print("yli 4 eur:")
    for tuote in hae(tuotteet, hinta_yli_4_euroa):
        print(tuote)

    print("keltaisia:")
    for tuote in hae(tuotteet2, keltainenko):
        print(tuote[0])  # tuplen eka