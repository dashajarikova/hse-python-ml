#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date


class Person:
    """
    >>> p = Person('Ivan', 'Ivanov', 'male', date(1989, 4, 26))
    >>> print(p)
    Ivan Ivanov, male, 29 years

    >>> p.full_ages()
    29
    >>> Person('Ivan', 'Ivanov', 'man', "1989.4.26")
    Traceback (most recent call last):
        ...
    ValueError: bday must be date type
    """

    def __init__(self, name, surname, sex, bday):
        raise NotImplementedError

    def full_ages(self):
        raise NotImplementedError


class Student:
    """
    >>> s = Student('Ivan', 'Ivanov', 'male', date(1989, 4, 26), 161, 9)
    >>> print(s)
    Ivan Ivanov, male, 29 years, 161 group, 9 skill
    """
    def __init__(self, name, surname, sex, bday, group, skill):
        raise NotImplementedError


class Group:
    """
    Encapsulates list of students
    """
    def sort_by_age(self, reverse=False):
        raise NotImplementedError

    def sort_by_skill(self, reverse=False):
        raise NotImplementedError

    def sort_by_age_and_skill(self, reverse=False):
        raise NotImplementedError


if __name__ == '__main__':
    import doctest
    doctest.testmod()
