#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from indivmodul import f1


if __name__ == '__main__':
    a1 = int(input("Введите сторуну a: "))
    b1 = int(input("Введите сторону b: "))
    h = int(input("Если вы хотите изменить type, напишите любое число, кроме нуля: "))
    fs = f1(h, a1, b1)
    print(fs(h))
