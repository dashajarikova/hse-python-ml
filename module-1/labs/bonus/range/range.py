#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class RangeIterator:

    def __init__(self, robj):
        raise NotImplementedError

    def __next__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError


class Range:

    def __init__(self, *args):
        raise NotImplementedError

    def count(self, value):
        raise NotImplementedError

    def index(self, value):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def __getitem__(self, key):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __contains__(self, key):
        raise NotImplementedError


if __name__ == "__main__":
    import doctest
    doctest.testmod()
