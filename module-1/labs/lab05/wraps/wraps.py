#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def wraps(*args, **kwargs):
    raise NotImplementedError


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@decorator
def foo(x):
    """Docstring foo"""
    return x


if __name__ == "__main__":
    print(foo("test"))
    print(foo.__doc__)
    print(foo.__name__)
    print(foo.__module__)
