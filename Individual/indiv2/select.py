#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select_1(list_trains, command_a):
    parts = command_a.split(' ', maxsplit=1)
    des = parts[1]
    result = []

    for train in list_trains:
        if train.get('destination') == des:
            result.append(train)

    return result
