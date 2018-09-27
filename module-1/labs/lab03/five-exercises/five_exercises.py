#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def map_(func, iterable):
    """
    The same as built-in map(), but generator

    >>> from collections import Generator
    >>> square = lambda x: x ** 2
    >>> isinstance(map_(square, range(10)), Generator)
    True
    >>> list(map_(square, range(10)))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    raise NotImplementedError


def zip_(*iterables):
    """
    The same as built-in zip(), but generator

    >>> for i, j, k in zip_(range(3), range(4), range(-7, 0)):
    ...     print(i, j, k)
    0 0 -7
    1 1 -6
    2 2 -5

    """
    raise NotImplementedError


def dropwhile(predicate, iterable):
    """
    The same as itertools.dropwhile(), but generator

    >>> from collections import Generator
    >>> isinstance(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]), Generator)
    True
    >>> list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
    [6, 4, 1]
    """
    raise NotImplementedError


def filterfalse(predicate, iterable):
    """
    The same as itertools.filterfalse(), but generator

    >>> from collections import Generator
    >>> isinstance(filterfalse(lambda x: x % 2, range(10)), Generator)
    True
    >>> list(filterfalse(lambda x: x % 2, range(10)))
    [0, 2, 4, 6, 8]
    """
    raise NotImplementedError


def unique(iterable):
    """
    Generates unique values from iterable object

    >>> from collections import Generator
    >>> issubclass(unique, Generator)
    True
    >>> list(unique([1, 1, 2, 2, 3, 1, 11, -1]))
    [1, 2, 3, 11, -1]
    """
    raise NotImplementedError


if __name__ == "__main__":
    import doctest
    doctest.testmod()
