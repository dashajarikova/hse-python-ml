#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
from copy import copy


class takes:
    raise NotImplementedError


if __name__ == "__main__":

    @takes(int, str, float, int)
    def foo(*args):
        print(args)

    try:
        args = 1, "arg1", 2.0, 11
        foo(*args)
    except TypeError as exc:
        print(str(exc))
    finally:
        print("It works a little something like.")

    @takes(int, float, str, int)
    def bar(*args):
        print(args)

    try:
        args = 1, "arg1", "kek", 12.0
        foo(*args)
    except TypeError as exc:
        print(str(exc))
    finally:
        print("It works a little something like.")
