def jarjesta_pisteiden_mukaan(alkiot):
    def jarjesta(alkio):
        return alkio["pisteet"]

    return sorted(alkiot, key=jarjesta, reverse = True)


def jarjesta_pisteiden_mukaan_lambda(alkiot):
    return sorted(alkiot, key=lambda alkio: alkio["pisteet"], reverse = True)

def jarjesta_pisteiden_muk_raja(alkiot, raja):
    kaikki = sorted(alkiot, key=lambda alkio: alkio["pisteet"], reverse = True)
    return [sarja for sarja in kaikki if sarja["pisteet"] > raja]

def jarjesta_kausien_mukaan_lambda(alkiot):
    return sorted(alkiot, key=lambda alkio: (alkio["kausia"], alkio["pisteet"]), reverse = True)



sarjat = [{ "nimi": "Dexter", "pisteet" : 8.6, "kausia":9 }, 
{ "nimi": "Friends", "pisteet" : 8.9, "kausia":10 },  
{ "nimi": "Simpsons", "pisteet" : 8.7, "kausia":32 } , 
{ "nimi": "South Park", "pisteet" : 8.1, "kausia":22 } , 
{ "nimi": "The Office", "pisteet" : 9.0, "kausia":9 }  ]

print("IMDB:n mukainen pistemäärä")
for sarja in jarjesta_pisteiden_mukaan(sarjat):
    print(f"{sarja['nimi']}  {sarja['pisteet']}")

print()
for sarja in jarjesta_pisteiden_mukaan_lambda(sarjat):
    print(f"{sarja['nimi']}  {sarja['pisteet']}")

print()
for sarja in jarjesta_kausien_mukaan_lambda(sarjat):
    print(f"{sarja['nimi']}  kausia:{sarja['kausia']}")

print("\nraja 8.5:")
for sarja in jarjesta_pisteiden_muk_raja(sarjat, 8.5):
    print(f"{sarja['nimi']}  {sarja['pisteet']}")