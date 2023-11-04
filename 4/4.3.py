def factorial(n):
    if n < 0:
        raise ValueError("Silnia jest zdefiniowana tylko dla liczb nieujemnych")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


print(factorial(4))
