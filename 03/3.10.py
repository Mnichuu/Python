
# Sposób 01: Używając pojedynczych przypisań do każdej liczby rzymskiej:
def sposob1(liczba_rzymska):
    cyfry_rzymskie = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }


# Sposób 02: Automatyczne tworzenie par indexów z liczbą w potędze 10 + statyczna 05
def sposob2(liczba_rzymska):
    cyfry_rzymskie = {litera: 10 ** exp for exp, litera in enumerate('IXCMVLD')}
    cyfry_rzymskie['V'] = 5


def roman2int(liczba_rzymska):
    cyfry_rzymskie = {
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
        aktualna = cyfry_rzymskie[litera]

        if poprzednia > aktualna:
            wynik -= aktualna
        else:
            wynik += aktualna

        poprzednia = aktualna

    return wynik


try:
    liczba_rzymska = "MCXL"
    arabska = roman2int(liczba_rzymska)
    print(arabska)  # Wynik: 2100
except ValueError as e:
    print(e)
