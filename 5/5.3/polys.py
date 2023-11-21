def add_poly(poly1, poly2):
    result = []
    len1, len2 = len(poly1), len(poly2)
    max_len = max(len1, len2)

    for i in range(max_len):
        term1 = poly1[i] if i < len1 else 0
        term2 = poly2[i] if i < len2 else 0
        result.append(term1 + term2)

    return result


def sub_poly(poly1, poly2):
    result = []
    len1, len2 = len(poly1), len(poly2)
    max_len = max(len1, len2)

    for i in range(max_len):
        term1 = poly1[i] if i < len1 else 0
        term2 = poly2[i] if i < len2 else 0
        result.append(term1 - term2)

    return result


def mul_poly(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]

    return result


def is_zero(poly):
    return all(coeff == 0 for coeff in poly)


def eq_poly(poly1, poly2):
    return poly1 == poly2


def eval_poly(poly, x0):
    result = 0
    for coeff in reversed(poly):
        result = result * x0 + coeff
    return result


def combine_poly(poly1, poly2):
    return [eval_poly(poly1, x) for x in poly2]


def pow_poly(poly, n):
    result = [1]
    for _ in range(n):
        result = mul_poly(result, poly)
    return result


def diff_poly(poly):
    result = [i * coeff for i, coeff in enumerate(poly) if i > 0]
    return result
