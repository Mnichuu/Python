
def f1():
    #sort() to metoda listy, która sortuje ją na miejsu, ale nic nie zwraca, więc L będzie None
    L = [3, 5, 4];
    #L = L.sort()
    return sorted(L)


def f2():
    #Za mało zmiennych dla przypisania 3 cyfr
    #x, y = 1, 2, 3
    x, y, z = 1, 2, 3
    return x,y,z

def f3():
    #Tuple są niemodyfikowalne
    X = 1, 2, 3;
    #X[1] = 4


def f4():
    #Nie ma takiego indeksu jak '3' w podanej tablicy
    X = [1, 2, 3];
    #X[3] = 4


def f5():
    #Metoda append jest dostępna tylko dla listy, a X jest napisem
    X = "abc";
    #X.append("d")


def f6():
    #Funkcja pow wymaga dwóch argumentów, ale nie jest poprawnie podawana do map
    #L = list(map(pow, range(8)))
    return list(map(lambda x: pow(x,2), range(8)))

print(f"Wynik funkcji 1: {f1()}")
print(f"Wynik funkcji 2: {f2()}")
print(f"Wynik funkcji 3: {f3()}")
print(f"Wynik funkcji 4: {f4()}")
print(f"Wynik funkcji 5: {f5()}")
print(f"Wynik funkcji 6: {f6()}")
