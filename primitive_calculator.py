# Uses python3
import sys

def optimal_sequence(n):
    sequence = [1]
    answer = [[0,1]]
    '''if n == 1:
        return sequence'''

    for i in range(2,n+1):
        if i % 3 == 0:
            a = answer[int(i/3 - 1)][0]
        else: a = sys.maxsize
        if i % 2 == 0:
            b = answer[int(i/2 - 1)][0]
        else: b = sys.maxsize
        c = answer[i - 2][0]
        x = list()
        y = list()
        if min(a,b,c) == a:
            x = x + answer[int(i/3 - 1)][1:]
            y.append(i)
            x = x + y
        elif min(a,b,c) == b:
            x = x + answer[int(i/2 - 1)][1:]
            y.append(i)
            x = x + y
        else:
            x = x + answer[i-2][1:]
            y.append(i)
            x = x + y
        z = list()
        z.append(min(a,b,c)+1)
        z = z + x
        answer.append(z)

    return answer[n-1][1:]

input = sys.stdin.read()
n = int(input)
sequence = optimal_sequence(n)
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
