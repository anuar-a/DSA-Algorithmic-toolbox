# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = len(points) * [0]
    a = list()
    b = list()
    x = list()
    y = 0
    left = 0
    right = 0
    for i in range(0,len(starts)):
        a.append(((starts[i]),"l"))
    for i in range(0,len(ends)):
        a.append(((ends[i]),"r"))
    for i in range(0,len(points)):
        a.append(((points[i]),"p",i))

    a.sort(key = lambda x:(x[0],x[1]))
    for i in a:
        if "l" in i:
            left = left + 1
        else:
            if "r" in i:
                right = right + 1
            else:
                cnt[int(i[2])] = left-right+y

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
