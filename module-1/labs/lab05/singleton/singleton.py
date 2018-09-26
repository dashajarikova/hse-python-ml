#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


def singleton(cls):
    raise NotImplementedError


if __name__ == "__main__":
    @singleton
    class A:
        pass
    print(A() is A() is A())
