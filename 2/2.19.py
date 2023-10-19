L = [7, 24, 60, 71, 101, 202, 300]

bloki = [str(liczba).zfill(3) for liczba in L]

wynik = ''.join(bloki)

print(wynik)

