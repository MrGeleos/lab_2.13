#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def display_train(list_trains):
    if list_trains:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "№",
                "Пункт",
                "Номер поезда",
                "Время отпраления"
            )
        )
        print(line)

        for idx, train in enumerate(list_trains, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                    idx,
                    train.get('destination', ''),
                    train.get('number', ''),
                    train.get('timer', '')
                )
            )
        print(line)
    else:
        print("Список пуст")
