# -*- coding: utf-8 -*-

from memory_profiler import profile


@profile(precision=4)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a



if __name__ == '__main__':
    """
    usage: python2 -m memory_profiler file.py
    """

    my_func()
