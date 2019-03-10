import sys


def chocolateFeast(n, c, m):
    a = 1
    count = 0
    count += n / c
    count1 = count
    while a and count >= m:
        count1 = count1 - m
        count += 1
        count1 += 1
        if count1 < m:
            a = 0
    return count

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n, c, m = raw_input().strip().split(' ')
        n, c, m = [int(n), int(c), int(m)]
        result = chocolateFeast(n, c, m)
        print result