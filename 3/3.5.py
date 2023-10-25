def rysuj_miarkę(dl):
    miarka = "|"
    cyfry = "0"

    for i in range(dl+1):
        miarka += "....|"
        if i > 9 and i < 99:
            cyfry += "   "
            if (len(cyfry) % 4 == 0):
                cyfry += str(int(i+1))
        else:
            cyfry += "    "
            if (len(cyfry) % 5 == 0):
                cyfry += str(int(i+1))


    print(miarka)
    print(cyfry)

# Przykładowe użycie:
dlugosc = 10
rysuj_miarkę(dlugosc)

