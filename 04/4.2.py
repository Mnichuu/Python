def rysuj_miarke(dl):
    spaces = 4

    miarka = "|"
    cyfry = "0"

    for i in range(dl):
        miarka += "....|"
        cyfry += "".zfill(spaces + 1 - len(str(i + 1))).replace('0', ' ') + str(i + 1)

    return miarka + "\n" + cyfry


def rysuj_prostokat(wysokosc, szerokosc):
    prostokat = ""

    for _ in range(wysokosc):
        prostokat += "+---" * szerokosc + "+\n"
        prostokat += "|   " * szerokosc + "|\n"

    prostokat += "+---" * szerokosc + "+\n"

    return prostokat


linijka = rysuj_miarke(15)
prost = rysuj_prostokat(5, 5)

print(linijka)
print(prost)
