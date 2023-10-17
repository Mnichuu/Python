line = "Patrzę na was, głodnych, przerażonych, przyciskających dzieci do pierśi"
wyrazy = line.split()

pierwsze_znaki = [wyraz[0] for wyraz in wyrazy]
ostatnie_znaki = []
for wyraz in wyrazy:
    ostatni_indeks = -1
    if wyraz[-1] == "," and len(wyraz) > 1:
        ostatni_indeks = -2
    ostatnie_znaki.append(wyraz[ostatni_indeks])

pierwsze_napis = "".join(pierwsze_znaki)
ostatnie_napis = "".join(ostatnie_znaki)

print(f"Napis z pierwszych znaków wyrazów z wiersza line: {pierwsze_napis}")
print(f"Napis z ostatnich znaków wyrazów z wiersza line: {ostatnie_napis}")
