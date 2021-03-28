#Uses python3

import sys
import queue
from collections import deque

def bipartite(adj):
    #write your code here
    dist = [0] * n
    prev = [0] * n
    for i in range(n):
        dist[i] = n+1
        #prev[i] = 0
    dist[0] = 0
    q = deque([0])
    while len(q) > 0:
        u = q.popleft()
        for i in adj[u]:
            if dist[i] == n+1:
                q.append(i)
                if dist[u] == 0:
                    dist[i] = 1
                elif dist[u] == 1:
                    dist[i] = 0
            elif dist[i] == dist[u]:
                return 0
            prev[i] = u
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
