#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


def print_files():
    if len(sys.argv) <= 1:
        print('Usage:', sys.argv[0], '<dir path>')
        return

    dir_ = sys.argv[1]
    raise NotImplementedError


if __name__ == "__main__":
    print_files()
