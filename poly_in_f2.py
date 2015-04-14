import exceptions
import fft


irreducible_poly = [1]


def delete_zero_high_order_coeffs(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()


def degree(poly):
    delete_zero_high_order_coeffs(poly)
    return len(poly) - 1 if poly[-1] else -1


def reminder(poly_a, poly_b):
    if degree(poly_b) == -1:
        raise exceptions.ZeroDivisionError
    poly_a = list(poly_a)
    
    while degree(poly_a) >= degree(poly_b):
        poly_a = sub(poly_a[::-1], poly_b[::-1], False)[::-1]
        delete_zero_high_order_coeffs(poly_a)
    return poly_a


def slow_mul(poly_a, poly_b):
    ret = [0] * (len(poly_a) + len(poly_b))
    for i, x in enumerate(poly_a):
        for j, y in enumerate(poly_b):
            ret[i + j] ^= x & y
    ret = reminder(ret, irreducible_poly)
    return ret


def mul(poly_a, poly_b):
    ret = fft.multiply(poly_a, poly_b)
    ret = [(x & 1) for x in ret]
    ret = reminder(ret, irreducible_poly)
    return ret


def poly_in_pow(poly, power):
    ret = [1]
    while power:
        if power & 1:
            ret = mul(ret, poly)
        poly = mul(poly, poly)
        power /= 2
    return ret


def inverse(poly):
    return poly_in_pow(poly, 2 ** degree(irreducible_poly) - 2)


def add(poly_a, poly_b, trim = True):
    ret = [0] * max(len(poly_a), len(poly_b))
    for i, x in enumerate(poly_a):
        ret[i] ^= x
    for i, x in enumerate(poly_b):
        ret[i] ^= x
    if trim:
        delete_zero_high_order_coeffs(ret)
    return ret


def sub(poly_a, poly_b, trim = True): 
    return add(poly_a, poly_b, trim)
