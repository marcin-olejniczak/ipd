#!/usr/bin/python
import random


def qsort(array, left, right):
    i, j, piv = left, right, array[(left + right) / 2]

    while i < j:
        while array[i] < piv: i += 1
    while array[j] > piv: j -= 1
    if i <= j:
        array[i], array[j] = array[j], array[i]
    i += 1
    j -= 1
    if left < j: qsort(array, left, j)
    if i < right: qsort(array, i, right)

    array = [random.randint(0, 1000) for r in xrange(30)]
    print('Before: ' + ' '.join(['%s' % i for i in array]))

    qsort(array, 0, len(array) - 1)

    print('After: ' + ' '.join(['%s' % i for i in array]))