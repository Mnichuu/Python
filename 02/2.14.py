line = "Patrzę na was, głodnych, przerażonych, przyciskających dzieci do pierśi"
wyrazy = line.split()
najdluzszy_wyraz = max(wyrazy, key=len)
dlugosc_najdluzszego_wyrazu = len(najdluzszy_wyraz)

print(f"Najdłuższy wyraz: {najdluzszy_wyraz}")
print(f"Długość najdłuższego wyrazu: {dlugosc_najdluzszego_wyrazu}")

