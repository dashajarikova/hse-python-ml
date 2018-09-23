#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class A:
    _init = 0

    def __init__(self, a, **kwargs):
        self._init += 1
        self.a = a
        for key, value in kwargs.items():
            setattr(self, key, value)


class B(A):
    _init = 0

    def __init__(self, a, b1, b2):
        self._init += 1
        A.__init__(self, a)
        self.b1 = b1
        self.b2 = b2


class C(A):
    _init = 0

    def __init__(self, a, c1, c2):
        self._init += 1
        A.__init__(self, a)
        self.c1 = c1
        self.c2 = c2


class D(B, C):
    _init = 0

    def __init__(self, a, b1, b2, c1, c2, d1, d2):
        self._init += 1
        B.__init__(self, a, b1, b2)
        C.__init__(self, a, c1, c2)
        self.d1 = d1
        self.d2 = d2


def main():
    pass


if __name__ == "__main__":
    main()
