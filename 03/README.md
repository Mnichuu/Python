ZADANIE 3.1
Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
for i in "axby": if ord(i) < 100: print (i)
for i in "axby": print (ord(i) if ord(i) < 100 else i)

ZADANIE 3.2
Co jest złego w kodzie:

L = [3, 5, 4] ; L = L.sort()
x, y = 1, 2, 3
X = 1, 2, 3 ; X[1] = 4
X = [1, 2, 3] ; X[3] = 4
X = "abc" ; X.append("d")
L = list(map(pow, range(8)))
ZADANIE 3.3
Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.

ZADANIE 3.4
Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

ZADANIE 3.5
Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12

ZADANIE 3.6
Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   | 
+---+---+---+---+

ZADANIE 3.7
Podany fragment programu pokaże problem z wyświetlaniem list obiektów stworzonych przez użytkownika, jeżeli nie została zdefiniowana metoda __repr__. Jeżeli zdefiniowano tylko metodę __repr__, to zostanie ona użyta również wtedy, gdy zwykle pracuje __str__. Sprawdzić działanie kodu, jeżeli wykomentujemy metodę __str__() lub metodę __repr__().
class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return "{} sec".format(self.s)

    def __repr__(self):
        return "Time({})".format(self.s)

time1 = Time(12)
time2 = Time(3456)
print("{} {}".format(time1, time2))   # Python wywołuje str()
print("{}".format([time1, time2]))   # Python wywołuje repr()

ZADANIE 3.8
Dla dwóch sekwencji liczb lub znaków znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń), (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

ZADANIE 3.9
Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. Znaleźć listę zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].

ZADANIE 3.10
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie (podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].