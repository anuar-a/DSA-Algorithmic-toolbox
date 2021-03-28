# Uses python3
def edit_distance(a, b):
    #write your code here
    count = 0
    D = [[0 for x in range(len(a)+1)] for y in range(len(b)+1)]
    L = []
    for i in range(len(a)+1):
        D[0][i] = i
    for i in range(len(b)+1):
        D[i][0] = i
    #print(D)
    #print(D[3][0])
    for j in range(1,len(b)+1):
        for i in range(1,len(a)+1):
            insertion = D[j-1][i] + 1
            deletion = D[j][i-1] + 1
            match = D[j-1][i-1]
            mismatch = D[j-1][i-1] + 1
            if a[i-1] == b[j-1]:
                D[j][i] = min(insertion,deletion,match)
            else:
                D[j][i] = min(insertion,deletion,mismatch)

    return D[len(b)][len(a)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
