line = "Patrzę na was, głodnych, przerażonych, przyciskających dzieci do pierśi"
wyrazy = line.split()

wyrazy_posortowane_alfabetycznie = sorted(wyrazy)

#sortowanie alfabetyczne?
print("Wyrazy posortowane alfabetycznie:")
for wyraz in wyrazy_posortowane_alfabetycznie:
    print(wyrazy)

wyrazy_posortowane_dlugoscia = sorted(wyrazy, key=len)

print("Wyrazy posortowane według długości:")
for wyraz in wyrazy_posortowane_dlugoscia:
    print(wyraz)
