# Uses python3
import sys
import random

'''def partition3(a, l, r):
    #write your code here
    x = a[l]
    j = l
    p = 1
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
            if a[j] == x:
                a[l+1], a[j] = a[j], a[l+1]
                p = p + 1
        print(a)
    k = p
    while p > 0:
        a[p], a[j + 1 - p] = a[j + 1 - p], a[p]
        p = p - 1
    return j+1-k, j'''

def partition3(a, l, r):
    x = a[l]
    p = l+1
    j = l

    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
            if a[j] < x:
                a[p], a[j] = a[j], a[p]
                p += 1

    a[l], a[p-1] = a[p-1], a[l]

    return p, j

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    #print(k)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    #print(m1,m2)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
