def rysuj_miarke(dl):
    miarka = "|"
    cyfry = "0"

    for i in range(dl):
        if len(str(miarka)) != len(str(cyfry)):
            cyfry += "   "
        else:
            cyfry += "    "
        if len(cyfry) % 5 == 0:
            cyfry += str(int(i+1))
        miarka += "....|"

    print(miarka)
    print(cyfry)


dlugosc = 12
rysuj_miarke(dlugosc)
