import poly_in_f2
import random


#random.seed = 20


def test_mul():
    poly_in_f2.irreducible_poly = [1, 0, 1, 0, 1]
    assert poly_in_f2.mul([1, 0, 1], [1, 0, 1]) == [0, 0, 1]
    assert poly_in_f2.mul([1, 0, 1], [0, 0, 1]) == [1]


def test_add():
    poly_in_f2.irreducible_poly = [1, 0, 1, 0, 1]
    assert poly_in_f2.add([1, 1, 1], [0, 1, 0]) == [1, 0, 1]


def test_reminder():
    assert poly_in_f2.reminder([1, 1, 0, 1], [1, 1]) == [1]
    assert poly_in_f2.reminder([0, 1, 0, 1], [1, 1]) == [0]


def test_inverse():
    poly_in_f2.irreducible_poly = [1, 1, 1]
    poly = [0, 1]
    assert poly_in_f2.mul(poly, poly_in_f2.inverse(poly)) == [1]
    poly = [1, 1]
    assert poly_in_f2.mul(poly, poly_in_f2.inverse(poly)) == [1]


def random_poly(n):
    a = [random.randrange(2) for i in xrange(n)]
    a[-1] = 1
    return a

