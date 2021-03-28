# Uses python3

import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(d,op):
    #write your code here
    global m
    global M
    m = [[0 for x in range(len(d))] for y in range(len(d))]
    M = [[0 for x in range(len(d))] for y in range(len(d))]
    for i in range(0,len(d)):
        m[i][i] = d[i]
        M[i][i] = d[i]

    for s in range(1,len(d)):
        for i in range (0,len(d)-s):
            j = i + s
            m[i][j],M[i][j] = min_and_max(i,j)

    return M[0][len(d)-1]

def min_and_max(i,j):
    mini = sys.maxsize
    maxi =  - sys.maxsize
    global ops
    global m
    global M

    for k in range(i,j):
        a =  evalt(M[i][k] ,M[k + 1][j], ops[k])
        b =  evalt(M[i][k] ,m[k + 1][j], ops[k])
        c =  evalt(m[i][k] ,M[k + 1][j], ops[k])
        d =  evalt(m[i][k] ,m[k + 1][j], ops[k])
        mini = min(mini, a, b, c, d)
        maxi = max(maxi, a, b, c, d)
    return (mini, maxi)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(input)
    #print(data)
    digits = list(map(int,data[0::2]))
    #print(digits)
    ops = list(data[1:-1:2])
    #print(ops)
    m = []
    M = []
    print(get_maximum_value(digits, ops))
