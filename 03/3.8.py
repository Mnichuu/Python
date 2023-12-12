A = [1, 2, 3, 4, 5]
B = [4, 5, 6, 7, 8]

wspolne_elementy = list(set(A) & set(B))
wszystkie_elementy = list(set(A) | set(B))

print("Wspólne elementy:", wspolne_elementy)
print("Wszystkie elementy:", wszystkie_elementy)
