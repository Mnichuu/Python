ZADANIE 4.2
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.

def make_ruler(n): pass

def make_grid(rows, cols): pass
ZADANIE 4.3
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

ZADANIE 4.4
Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

ZADANIE 4.5
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

ZADANIE 4.6
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

ZADANIE 4.7
Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości. Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))   # [1,2,3,4,5,6,7,8,9]