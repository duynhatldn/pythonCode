
import math
import os
import random
import re
import sys


def spl_question(arr, n, k):
    prev_accum = cumm = tot_pg_num = ques = count = 0

    for each_chptr in arr:

        pgs, rem = divmod(each_chptr, k)
        ques = prev_accum = cumm = 0
        for pg in xrange(pgs):
            tot_pg_num += 1
            ques += k
            cumm = ques
            if prev_accum < tot_pg_num <= cumm:
                count += 1
            prev_accum = cumm
        if rem:
            tot_pg_num += 1
            ques += rem
            cumm = ques
        if prev_accum < tot_pg_num <= cumm:
            count += 1
    return count

if __name__ == "__main__":
    n, k = raw_input().strip("\n").split()
    n, k = int(n), int(k)

    arr = map(int, raw_input().strip("\n").split())

    print spl_question(arr, n, k)
