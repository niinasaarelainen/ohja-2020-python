def summa(luku: int):
    if luku==1:
        return 1
    else:
        return luku + summa(luku -1)