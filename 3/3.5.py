def rysuj_miarkę(dl):
    miarka = "|"
    cyfry = "0"

    for i in range(dl):
        if i > 9 and i < 99:
            cyfry += "   "
        else:
            cyfry += "    "
        if (len(cyfry) % 5 == 0):
            cyfry += str(int(i+1))
        miarka += "....|"

    print(miarka)
    print(cyfry)

# Przykładowe użycie:
dlugosc = 12
rysuj_miarkę(dlugosc)
