#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    count = 0
    D = [[0 for x in range(len(b)+1)] for y in range(len(a)+1)]
    L = []
    for i in range(len(a)+1):
        D[i][0] = 0
    for i in range(len(b)+1):
        D[0][i] = 0
    #print(D)
    #print(D[3][0])
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1] == b[j-1]:
                D[i][j] = D[i-1][j-1] + 1
            else:
                D[i][j] = max(D[i-1][j],D[i][j-1])

    return D[len(a)][len(b)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
