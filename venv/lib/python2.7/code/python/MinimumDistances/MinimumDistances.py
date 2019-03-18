import math
import os
import random
import re
import sys

def minimumDistances(a):
    md=len(a)
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if(a[i]==a[j] and j-i<md):
                md=j-i
    if(md==len(a)):
        return -1
    else:
        return md


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
