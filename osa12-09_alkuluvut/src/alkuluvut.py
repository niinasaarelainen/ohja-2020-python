def alkuluku(luku):
    for jakaja in range(2, int(luku/2)+1): # suurin luku millä numero voi olla jaollinen on puolet itsestä
        if luku % jakaja == 0:
            return False
    return True

def alkuluvut():
    luku = 1
    while True:
        if alkuluku(luku):
            yield luku
        luku += 1    




if __name__ == "__main__":
    luvut = alkuluvut()
    for i in range(9):
        print(next(luvut)) 