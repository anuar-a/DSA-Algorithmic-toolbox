# Uses python3
import sys

def optimal_summands(n):
    summands = []
    sum = 0
    i = 0
    #write your code here
    if n == 1:
        return '1'

    else:
        for i in range(1,n+1):
            if sum + i <= n:
                sum = sum + i
                summands.append(i)
            else:
                summands.remove(i-1)
                sum = sum - i + 1
                summands.append(n-sum)
                break
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
