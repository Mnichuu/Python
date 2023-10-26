def roman2int(liczba_rzymska):
    rzadkie_rzymskie = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    wynik = 0
    poprzednia = 0

    for litera in liczba_rzymska[::-1]:
        aktualna = rzadkie_rzymskie[litera]

        if poprzednia > aktualna:
            wynik -= aktualna
        else:
            wynik += aktualna

        poprzednia = aktualna

    return wynik


# Przykładowe użycie:
rzymska = "MMMM"
arabska = roman2int(rzymska)
print(arabska)
