import re

def on_viikonpaiva(merkkijono: str):
    lauseke = re.compile("ma|ti|ke|to|pe|la|su")
    if lauseke.search(merkkijono):
        return True
    return False

def kaikki_vokaaleja(merkkijono: str):
    if merkkijono == "":
        return False
    lauseke = re.compile("[aeiouyäöå]")  
    for merkki in  merkkijono:
         if not lauseke.search(merkki):
            return False
    return True

def kellonaika(merkkijono: str):
    lauseke1_yleis = re.compile("[0-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}:[0-5]{1}[0-9]{1}")  
    lauseke2_tunnit = re.compile("^[2]{1}[4-9]{1}")
    if lauseke2_tunnit.search(merkkijono):
        return False
    if lauseke1_yleis.search(merkkijono):
        return True
    return False


if __name__ == "__main__":
    print(on_viikonpaiva("ma"))
    print(on_viikonpaiva("pe"))
    print(on_viikonpaiva("tu"))
    print(on_viikonpaiva("su"))
    print(on_viikonpaiva("suu"))
    print(on_viikonpaiva(""))

    print("kaikki_vokaaleja:")
    print(kaikki_vokaaleja("eioueioieoieouyyyy"))
    print(kaikki_vokaaleja("autoooo"))
    print(kaikki_vokaaleja("ööööööö"))
    print(kaikki_vokaaleja("moi"))
    print(kaikki_vokaaleja(""))

    print("kellonaika:")
    print(kellonaika("12:43:01"))
    print(kellonaika("17:59:59"))
    print(kellonaika("00:43:01"))
    print(kellonaika("25:59:59"))   # pitäisi olla False
    print(kellonaika("33:66:77"))
    print(kellonaika(""))