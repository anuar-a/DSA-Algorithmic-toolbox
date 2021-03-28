#Uses python3
import sys
import math

def distance(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def minimum_distance(x, y, points):
    result = 0.
    #write your code here
    cost = [float('inf')] * n
    parents = [0] * n
    prioq = []
    cost[0] = 0
    for i in range(n):
        prioq.append([cost[i],i])
    while len(prioq) > 0:
         v = min(prioq)
         for i in range(n):
             if i in [i[1] for i in prioq] and i != v[1] and cost[i] > distance(points[v[1]],points[i]):
                 cost[i] = distance(points[v[1]],points[i])
                 parents[i] = v[1]
                 for j in prioq:
                     if j[1] == i:
                         prioq[prioq.index(j)][0] = cost[i]
         prioq.remove(v)
         if len(prioq) > 0:
             x = min(prioq)
             result = result + x[0]
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = []
    for i in range(n):
        points.append([x[i],y[i]])
    print("{0:.9f}".format(minimum_distance(x, y, points)))
