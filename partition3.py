# Uses python3
import sys
import itertools

def partition3(C,X,n):
    global A
    if len(C) == 0:
        return 1
    # write your code here
    D = [[0 for x in range(int(sum(C)/n) + 1)] for y in range(len(C) + 1)]
    B = []
    B = B + C
    for i in range(1,len(C) + 1):
        for j in range(1,int(sum(C)/n) + 1):
            D[i][j] = D[i-1][j]
            if C[i-1] <= j:
                val = D[i-1][j-C[i-1]] + C[i-1]
                if D[i][j] < val:
                    D[i][j] = val
    '''with open('test2.xls', 'w') as f:
        for item in D:
            f.write("%s\n" % item)'''
    k = int(sum(C)/n)
    for i in reversed(range(1,len(C) + 1)):
        #print(A[i-1])
        if C[i-1] <= k:
            if (D[i-1][k-C[i-1]] + C[i-1]) >= D[i-1][k]:
                X.append(C[i-1])
                B.pop(i-1)
                if k <= 0: break
                k = k-C[i-1]
    #print(sum(X),X)
    #print(sum(B),B)
    #print(sum(A))
    #print(sum(A)/n)
    #if int(sum(A)*(4-n)/3) + int(sum(A)*(n-1)/3) != int(sum(A)):
    if int(sum(X)) != int(sum(A)*(4-n)/3):
        return 0
    #Z = [item for item in A if not item in X or X.remove(item)]
    #Z = [item for item in A + X if item not in A or item not in X]print(X)
    #print(Z)
    #print('*****************')
    return partition3(B,X,n-1)
    #return D[len(A)][int(sum(A)/n)]

    #return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    A.sort()
    Y = []
    if sum(A) % 3 == 0:
        print(partition3(A,Y,3))
    else: print(0)
