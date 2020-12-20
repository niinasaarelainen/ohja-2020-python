def parilliset(alku: int, maksimi: int):
    luku = alku
    if luku % 2 != 0:
        luku += 1
    while luku <= maksimi:
        yield luku
        luku += 2




if __name__ == "__main__":
    luvut = parilliset(2, 10)
    for luku in luvut:
        print(luku)

    luvut = parilliset(11, 21)
    for luku in luvut:
        print(luku)