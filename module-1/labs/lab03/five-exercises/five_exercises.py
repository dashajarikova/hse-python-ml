#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def map_(func, iterable):
    """
    The same as built-in map()
    """
    raise NotImplementedError


def zip_(*args):
    """
    The same as built-in zip()
    """
    raise NotImplementedError


def dropwhile(predicate, iterable):
    """
    The same as itertools.dropwhile()
    """
    raise NotImplementedError


def filterfalse(predicate, iterable):
    """
    The same as itertools.filterfalse()
    """
    raise NotImplementedError


def unique(iterable):
    raise NotImplementedError


if __name__ == "__main__":
    import doctest
    doctest.testmod()
