def sum_seq(sequence):
    total_sum = 0

    for item in sequence:
        if isinstance(item, (list, tuple)):
            total_sum += sum_seq(item)
        else:
            total_sum += item

    return total_sum


seq = [1, 2, [3, 4], (5, 6), [7, 8, [9, 10]]]
print(sum_seq(seq))
