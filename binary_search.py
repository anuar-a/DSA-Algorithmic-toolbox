# Uses python3
import sys

def binary_search(a, left, right, x):
    if right < left :
        return -1
    mid = round((right + left)/2)
    if x == a[mid-1]:
        return mid - 1
    else :
        if x < a[mid-1]:
            return binary_search(a, left, mid - 1, x)
        else:
            return binary_search(a, mid + 1, right, x)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, 1, len(a), x), end = ' ')
