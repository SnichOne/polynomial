#!/usr/bin/env python

import poly_in_f2
import poly


def init_irreducible_poly():
    with open('poly.txt') as myfile:
        poly_in_f2.irreducible_poly = poly.int_poly_from_str(myfile.readline())


def calc_operation():
    with open('input.txt') as myfile:
        lines = myfile.readlines(3)
        operator = lines[0][:-1]
        if operator == 'reminder':
            ret = poly_in_f2.reminder(poly.int_poly_from_str(lines[1]),
                                      poly.int_poly_from_str(lines[2]))
        elif operator == 'inverse':
            ret = poly_in_f2.inverse(poly.int_poly_from_str(lines[1]))
        elif operator == '+':
            ret = poly_in_f2.add(poly.int_poly_from_str(lines[1]),
                                 poly.int_poly_from_str(lines[2]))
        elif operator == '*':
            ret = poly_in_f2.mul(poly.int_poly_from_str(lines[1]),
                                 poly.int_poly_from_str(lines[2]))
        elif operator == 'pow':
            ret = poly_in_f2.poly_in_pow(poly.int_poly_from_str(lines[1]),
                                         int(lines[2]))
        else:
            ret = 'invalid operation'
        return ret


def main():
    init_irreducible_poly()
    ret = calc_operation()
    print ret


if __name__ == '__main__':
    main()
