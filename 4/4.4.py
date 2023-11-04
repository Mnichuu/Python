def fibonacci(n):
    if n < 0:
        raise ValueError("Ciąg Fibonacciego jest zdefiniowany tylko dla liczb nieujemnych")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_n_minus_2 = 0
        fib_n_minus_1 = 1

        for i in range(2, n + 1):
            fib_n = fib_n_minus_1 + fib_n_minus_2
            fib_n_minus_2, fib_n_minus_1 = fib_n_minus_1, fib_n

        return fib_n


print(fibonacci(5))
