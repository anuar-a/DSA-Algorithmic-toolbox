# Uses python3
import sys

def get_change(m):
    n = 0
    while m > 0:
        if m >= 10:
            n = n + 1
            m = m - 10
        else:
             if m >= 5:
                 n = n + 1
                 m = m - 5
             else :
                 n = n + 1
                 m = m - 1
    return n

m = input()
print(get_change(int(m)))
