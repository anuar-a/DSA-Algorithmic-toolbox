#Uses python3
import sys
import math

def distance(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def make_set(i,parent,rank):
    parent[i] = i
    rank[i] = 0

def find(i,parent):
    if i != parent[i]:
        parent[i] = find(parent[i],parent)
    return parent[i]

def union(i,j,parent,rank):
    i_id = find(i,parent)
    j_id = find(j,parent)
    if i_id == j_id:
        return
    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
    else:
        parent[i_id] = j_id
        if rank[i_id] == rank[j_id]:
            rank[j_id] = rank[j_id] + 1

def clustering(points, k):
    #write your code here
    parent = [0] * n
    rank = [0] * n
    edges = []
    for i in range(len(points)):
        make_set(i,parent,rank)
    X = []
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                edges.append([i,j,distance(points[i],points[j])])
    edges.sort(key = lambda x:x[2])

    for i in edges:
        if find(i[0],parent) != find(i[1],parent):
            X.append(i)
            union(i[0],i[1],parent,rank)
    return X[-k+1][2]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    points = []
    for i in range(n):
        points.append([x[i],y[i]])
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(points, k)))
