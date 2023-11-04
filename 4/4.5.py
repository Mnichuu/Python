def odwracanie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_r(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_r(L, left + 1, right - 1)


lista = [1, 2, 3, 4, 5, 6, 7]
odwracanie(lista, 2, 5)
print(lista)
lista_r = [1, 2, 3, 4, 5, 6, 7]
odwracanie_r(lista_r, 1, 6)
print(lista_r)
