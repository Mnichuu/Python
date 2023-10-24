
def f1():
    #sort() to metoda listy, która sortuje ją na miejsu, ale nic nie zwraca, więc L będzie None
    L = [3, 5, 4];
    #L = L.sort()
    return L.sort()


def f2():
    #za mało zmiennych dla przypisania 3 cyfr
    #x, y = 1, 2, 3
    x, y, z = 1, 2, 3
    return x,y,z

def f3():
    X = 1, 2, 3;
    X[1] = 4


def f4():
    X = [1, 2, 3];
    X[3] = 4


def f5():
    X = "abc";
    X.append("d")


def f6():
    L = list(map(pow, range(8)))


print(f"Wynik funkcji 1: {f1()}")
print(f"Wynik funkcji 2: {f2()}")
print(f"Wynik funkcji 3: {f3()}")
print(f"Wynik funkcji 4: {f4()}")
print(f"Wynik funkcji 5: {f5()}")
print(f"Wynik funkcji 6: {f6()}")
