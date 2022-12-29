#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_train(list_trains):
    destination = input("Пункт назначения? ")
    number = input("Номер поезда? ")
    timer = input("Время отправления (ЧЧ:ММ)? ")

    train = {
        'destination': destination,
        'number': number,
        'timer': timer,
    }

    list_trains.append(train)
    if len(list_trains) > 1:
        list_trains.sort(key=lambda item: item.get('timer', ''))
    return list_trains
