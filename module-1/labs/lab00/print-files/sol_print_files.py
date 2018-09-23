#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


def print_files():
    if len(sys.argv) <= 1:
        print('Usage:', sys.argv[0], '<dir path>')
        return

    dir_path = sys.argv[1]
    file_data = []
    for name in os.listdir(dir_path):
        path = os.path.join(dir_path, name)
        if not os.path.isfile(path):
            continue
        st = os.stat(path)
        file_data.append([name, st.st_size])

    file_data.sort(key=lambda x: (-x[1], x[0]))
    for name, size in file_data:
        print(name + '\t' + str(size))


if __name__ == "__main__":
    print_files()
