import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = raw_input().split()
    arr = map(int, arr)
    arr.sort()
    s = sum(arr)
    maxV = s - arr[0]
    minV = s - arr[4]
    print ('%d %d' % (minV, maxV))