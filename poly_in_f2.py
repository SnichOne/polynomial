import exceptions


irreducible_poly = [1]


def trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    while len(poly) >= len(irreducible_poly):
        poly = sub(poly, irreducible_poly)
    return poly


def degree(poly):
    trim(poly)
    return len(poly) - 1 if poly[-1] else -1


def reminder(poly_a, poly_b):
    if degree(poly_b) == -1:
        raise exceptions.ZeroDivisionError
    poly_a = list(poly_a)
    
    while degree(poly_a) >= degree(poly_b):
        poly_a = sub(poly_a[::-1], poly_b[::-1])[::-1]
        trim(poly_a)
    return poly_a


def mul(poly_a, poly_b):
    ret = [0] * (len(poly_a) + len(poly_b))
    for i, x in enumerate(poly_a):
        for j, y in enumerate(poly_b):
            ret[i + j] ^= x & y
    return trim(ret)


def poly_in_pow(poly, power):
    ret = [1]
    while power:
        if power & 1:
            ret = mul(ret, poly)
        poly = mul(poly, poly)
        power /= 2
    return trim(ret)


def inverse(poly):
    return poly_in_pow(poly, 2 ** degree(irreducible_poly) - 2)


def add(poly_a, poly_b):
    ret = [0] * max(len(poly_a), len(poly_b))
    for i, x in enumerate(poly_a):
        ret[i] ^= x
    for i, x in enumerate(poly_b):
        ret[i] ^= x
    return trim(ret)


def sub(poly_a, poly_b): 
    return add(poly_a, poly_b)
