#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


def cached(*args, **kwargs):
    """
    >>> @cached
    ... def add(a, b):
    ...     print(a, b)
    ...     return a + b
    ...
    >>> add(1, 2)
    1 2
    3
    >>> add(1, 2)
    3
    >>> add(2, 2)
    2 2
    4
    >>> add(2, 2)
    4
    """
    raise NotImplementedError


if __name__ == '__main__':
    import doctest
    doctest.testmod()
