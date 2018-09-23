#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def divisible(begin, end):
    """
    :param begin: int, positive integer
    :param end: int, positive integer
    :return: str, string of space separated integers

    Examples of usage:
    >>> divisible(1, 10)
    '7'
    >>> divisible(1, 17)
    '7 14'
    >>> len(divisible(100, 1000))
    407
    >>> divisible(29, 60)
    '42 49 56'
    >>> len(divisible(300, 3000).split())
    309
    >>> ns = [int(n) for n in divisible(300, 10000).split()]
    >>> seven_mask = [not bool(n % 7) for n in ns]
    >>> all(seven_mask)
    True
    >>> any(seven_mask)
    True
    >>> five_mask = [not bool(n % 5) for n in ns]
    >>> all(five_mask)
    False
    >>> any(five_mask)
    False
    >>> divisible(2, 5)
    ''
    >>> 1329 not in ns
    True
    """
    result = []
    for number in range(begin, end + 1):
        if number % 7 == 0 and number % 5 != 0:
            result.append(str(number))
    return " ".join(result)


def register_count(string):
    """
    :param string: str, input string
    :return: dict, dict of lower and upper letter counts

    >>> register_count("Mama") == {'UPPER': 1, 'LOWER': 3}
    True
    >>> register_count("Your Name") == {'UPPER': 2, 'LOWER': 6}
    True
    >>> register_count("LingvoX!!!") == {'UPPER': 2, 'LOWER': 5}
    True
    >>> register_count("Trud, mir, mai! Zvahka!") == {'UPPER': 2, 'LOWER': 14}
    True
    >>> register_count("Coi ZIV!,,,,,") == {'UPPER': 4, 'LOWER': 2}
    True
    """
    register = {"UPPER": 0, "LOWER": 0}
    for c in string:
        if c.isupper():
            register["UPPER"] += 1
        elif c.islower():
            register["LOWER"] += 1
        else:
            pass
    return register


def pairwise_diff(first, second):
    """

    :param first: str, first input string
    :param second: str, second input string
    :return: float, percentage of different letters

    >>> pairwise_diff('ABSD', 'ABCD')
    0.25
    >>> pairwise_diff('aBSD', 'ABCD')
    0.5
    >>> pairwise_diff('LingvX', 'SpaceX')
    0.83
    >>> pairwise_diff('LingvoX', 'SpaceX')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> pairwise_diff('abc', 'ab')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> first = 'Salaman..'; second = 'Salaman.!'
    >>> round(1. / len(first), 2) == pairwise_diff(first, second)
    True
    >>> pairwise_diff(first + second, first + first)
    0.06
    >>> pairwise_diff(first * 3, second * 2 + first)
    0.07
    """
    assert len(first) == len(second)

    n_diffs = 0
    for fchr, schr in zip(first, second):
        if fchr != schr:
            n_diffs += 1
    return round(n_diffs / len(first), 2)


def run_robot():
    """
    Uses input() inside.
    :return: int, rounded euclidean distance from origin
    """
    pos_x, pos_y = 0, 0
    while True:
        s = input()
        if not s:
            break
        movement = s.split(" ")
        direction = movement[0]
        steps = int(movement[1])
        if direction == "UP":
            pos_y += steps
        elif direction == "DOWN":
            pos_y -= steps
        elif direction == "LEFT":
            pos_x -= steps
        elif direction == "RIGHT":
            pos_x += steps
        else:
            pass
    return int(round(math.sqrt(pos_x ** 2 + pos_y ** 2)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
