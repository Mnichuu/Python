line = "Patrzę na was, głodnych, przerażonych, przyciskających dzieci do pierśi"
wynik = 0

for wyraz in line.split():
    if wyraz[-1] == "," and len(wyraz) > 1:
        wynik = wynik - 1
    lenght = len(wyraz)
    wynik = wynik + lenght

print(f" Łączna ilośc wyrazów policzona tradycyjnie: {wynik} ")

wynik_sum = sum(len(wyraz) - (1 if wyraz[-1] == "," else 0) for wyraz in line.split())

print(f" Łączna ilośc wyrazów policzona za pomocą funkcji sum(): {wynik_sum} ")
