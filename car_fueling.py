# python3
import sys


def compute_min_refills(L, m, n, stops):
    # write your code here
    numRefills = 0
    currentRefill = 0
    stops.insert(0,0)
    stops.append(L)
    while currentRefill <= n:
        lastRefill = currentRefill
        while currentRefill <= n and (stops[int(currentRefill) + 1] - stops[int(lastRefill)]) <= m:
            currentRefill = currentRefill + 1
        if currentRefill == lastRefill:
            return -1
        if currentRefill <= n:
            numRefills = numRefills + 1
    return numRefills

if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, n, stops))
