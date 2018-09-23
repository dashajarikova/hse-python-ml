#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


class Ocean:

    def __init__(self, init_state):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def gen_next_quantum(self):
        raise NotImplementedError


if __name__ == '__main__':
    n_quantums = int(sys.stdin.readline())
    n_rows, n_clms = [int(i) for i in sys.stdin.readline().split()]
    init_state = []
    for i in range(n_rows):
        line = [int(i) for i in sys.stdin.readline().split()]
        init_state.append(line)

    ocean = Ocean(init_state=init_state)
    for _ in range(n_quantums):
        ocean = ocean.gen_next_quantum()
    print(ocean)
