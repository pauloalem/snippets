# -*- coding: utf-8
"""Quickfind implementation"""

def connect(L, p, q):
    Lp, Lq = L[p], L[q]
    for i, l in enumerate(L):
        if L[i] == Lp:
            L[i] = Lq
    return L


def is_connected(L, p, q):
    return L[p] == L[q]


if __name__ == '__main__':
    data = range(10)

    assert is_connected(data, 1, 1)
    assert not(is_connected(data, 1, 2))

    assert connect(data, 0, 4) == [4, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert connect(data, 0, 9) == [9, 1, 2, 3, 9, 5, 6, 7, 8, 9]
    assert connect(data, 1, 7) == [9, 7, 2, 3, 9, 5, 6, 7, 8, 9]
    assert connect(data, 9, 1) == [7, 7, 2, 3, 7, 5, 6, 7, 8, 7]
    assert connect(data, 7, 8) == [8, 8, 2, 3, 8, 5, 6, 8, 8, 8]
    assert connect(data, 3, 1) == [8, 8, 2, 8, 8, 5, 6, 8, 8, 8]
    assert connect(data, 2, 6) == [8, 8, 6, 8, 8, 5, 6, 8, 8, 8]

    assert is_connected(data, 1, 1)
    assert is_connected(data, 2, 6)
    print data
