#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from indiv2.add import get_train
from indiv2.help_1 import help_1
from indiv2.list import display_train
from indiv2.select import select_1


def main():
    trains = []

    while True:
        command = input(">>> ").lower()
        if command == "exit":
            break
        elif command == "add":
            trains = get_train(trains)
        elif command == "list":
            display_train(trains)
        elif command.startswith('select '):
            selected = select_1(trains, command)
            display_train(selected)
        elif command == "help":
            help_1()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
