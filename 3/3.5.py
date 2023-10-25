def rysuj_miarkę(dl):
    miarka = "|"
    cyfry = ""

    for i in range(5*(dl) + 1):
        if i % 5 == 0 and int(i/5) < 10:
            miarka += "|"
            cyfry += str(int(i/5))
        else:
                miarka += "."
                cyfry += " "




    print(miarka)
    print(cyfry)

# Przykładowe użycie:
dlugosc = 19
rysuj_miarkę(dlugosc)

