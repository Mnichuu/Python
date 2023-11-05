def flatten(sequence):
    flattened = []

    for item in sequence:
        if isinstance(item, (list, tuple)):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)

    return flattened

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(seq))  # Wynik: [1, 2, 3, 4, 5, 6, 7, 8, 9]
