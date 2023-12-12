def rysuj_prostokat(wysokosc, szerokosc):
    prostokat = ""

    for _ in range(wysokosc):
        prostokat += "+---" * szerokosc + "+\n"
        prostokat += "|   " * szerokosc + "|\n"

    prostokat += "+---" * szerokosc + "+\n"

    print(prostokat)


rysuj_prostokat(10, 10)
