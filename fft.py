import math


def list_to_complex(a):
    return [complex(x) for x in a]


def fix_length(a, b):
    n = 1
    while n < max(len(a), len(b)):
        n <<= 1
    n <<= 1
    a.extend([0] * (n - len(a)))
    b.extend([0] * (n - len(b)))


def butterfly(c, a, b):
    return (a + c * b, a - c * b)


def fft(a, invert):
    n = len(a)
    if n == 1:
        return
    a_even = a[::2]
    a_odd = a[1::2]
    fft(a_even, invert)
    fft(a_odd, invert)
    root = complex(1)
    angle = 2 * math.pi / n
    if invert:
        angle = -angle
    generative_root = complex(math.cos(angle), math.sin(angle))
    for i in xrange(len(a_even)):
        (a[i], a[i + n / 2]) = butterfly(root, a_even[i], a_odd[i])
        if invert:
            a[i] /= 2
            a[i + n / 2] /= 2
        root *= generative_root


def multiply(a, b):
    fa = list_to_complex(a)
    fb = list_to_complex(b)
    fix_length(fa, fb)

    fft(fa, False)
    fft(fb, False)
    for i, y in enumerate(fb):
        fa[i] *= y
    fft(fa, True)
    return [int(x.real + 0.5) for x in fa]
