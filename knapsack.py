# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    D = [[0 for x in range(W + 1)] for y in range(len(w) + 1)]

    for i in range(1,len(w) + 1):
        for j in range(1,W + 1):
            D[i][j] = D[i-1][j]
            if w[i-1] <= j:
                val = D[i-1][j-w[i-1]] + w[i-1]
                if D[i][j] < val:
                    D[i][j] = val

    for i in D:
        print(i)
    return D[len(w)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
