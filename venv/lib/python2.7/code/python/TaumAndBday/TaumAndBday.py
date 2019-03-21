

import math
import os
import random
import re
import sys


def taumBday(b, w, x, y, z):
    if x == y:
        return (b + w) * x
    elif x > y and x > (z + y):
        return ((b * (z + y)) + w * y)
    elif y > x and y > (z + x):
        return (b * x + (w * (z + x)))
    else:
        return (b * x + w * y)

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        b, w = raw_input().strip().split(' ')
        b, w = [int(b), int(w)]
        x, y, z = raw_input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = taumBday(b, w, x, y, z)
        print result