#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def f1(l, a, b):
    type = 0

    if l != 0:
        type = l
    else:
        print("Type не изменился")

    def f2(s):
        if type == 0:
            s = 1/2 * (a * b)
            return s
        else:
            s = a * b
            return s

    return f2
