
def rysuj_miarke(dl):
    spaces = 4

    miarka = "|"
    cyfry = "0"

    for i in range(dl):
        miarka += "....|"
        cyfry += "".zfill(spaces + 1 - len(str(i+1))).replace('0', ' ') + str(i+1)

    print(miarka)
    print(cyfry)


user_input = input("Podaj rozmiar miarki: ")

try:
    rysuj_miarke(int(user_input))
except ValueError:
    print("Wprowadź poprawną liczbę całkowitą.")
