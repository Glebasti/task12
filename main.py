#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from time import time

array = [0] * 1_000_000


def pull_integer_data(array):
    for i in range(len(array)):
        array[i] = randint(0, 999)
    return array


array = pull_integer_data(array)


def calcHist(tdata):
    hist = [0] * 10
    for data in tdata:
        hist[data // 100] += 1
    return hist


a = calcHist(array)
print(a)

count_time = [0] * 100

for i in range(100):
    start = time()
    calcHist(array)
    end = time()
    count_time[i] = end - start

mean_time = 0
# Расчёт среднего времени
for i in range(100):
    mean_time += count_time[i]

print(f"Минимальное время: {min(count_time)}")
print(f"Среднее время: {mean_time / 100}")
print(f"Максимальное время: {max(count_time)}")
