import os
import sys


def bigSorting(unsorted):
    return sorted(unsorted)


if __name__ == '__main__':
    n = int(raw_input())

    unsorted = []

    for _ in xrange(n):
        unsorted_item = raw_input()
        unsorted.append(long(unsorted_item))

    result = bigSorting(unsorted)

    for x in result:
        print(x)