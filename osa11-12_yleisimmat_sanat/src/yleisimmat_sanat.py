def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    f = open(tiedoston_nimi, "r") 
    str = ""
    for rivi in f:
        str += rivi

    str = str.replace("\n", " ")  # huom ei "" muuten rivinvaihdoissa tulee yhdyssanoja
    clean_str=  "".join([merkki for merkki in str if merkki not in ".,"])

    
    splitted = clean_str.split(" ")
    return {sana : splitted.count(sana) for sana in splitted if splitted.count(sana) >= raja}
    


if __name__ == "__main__":
    print(yleisimmat_sanat("comprehensions.txt", 3))
    print(yleisimmat_sanat("programming.txt", 3))