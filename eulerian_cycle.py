#python3

import sys
import queue

sys.setrecursionlimit(200000)

def dfs(adj,visited):
    explore(0,adj,visited)
    return visited

def explore(v,adj,visited):
    visited[v] = True
    for i in adj[v]:
        if visited[i] == False:
            explore(i,adj,visited)
    return visited

def find_path(visits,adj,edges):
    m = len(edges)
    ind = 0
    val = 0
    for i in range(len(visits)):
        if visits[i] >= val:
            ind = i
            val = visits[i]
    path = [0]
    while len(path) != m:
        ind_unvisited = -1
        num_unvisited = 0
        for i in adj[path[-1]]:
            if visits[i] > num_unvisited and (path[-1] + 1,i + 1) in edges:
                ind_unvisited = i
                num_unvisited = visits[i]
        if ind_unvisited == -1:
            break
        next_vertex = ind_unvisited
        visits[path[-1]] -= 1
        edges.remove((path[-1]+1,next_vertex+1))
        path.append(next_vertex)
    return [i+1 for i in path]

def eulerian_cycle(visits,adj,edges):
    edge_count = [0] * len(adj)
    curr_path = []
    circuit = []
    for i in range(len(adj)):
        edge_count[i] = len(adj[i])
    curr_path.append(0)
    curr_v = 0
    while len(curr_path) > 0:
        if edge_count[curr_v] > 0:
            curr_path.append(curr_v)
            next_v = adj[curr_v][-1]
            edge_count[curr_v] -= 1
            adj[curr_v].pop()
            curr_v = next_v
        else:
            circuit.append(curr_v)
            curr_v = curr_path[-1]
            curr_path.pop()
    circuit.reverse()
    circuit.pop()
    return [i+1 for i in circuit]

def balanced(balance):
    for i in balance:
        if i != 0:
            return False
    return True

def strongly_connected(visited):
    if False in visited:
        return False
    else:
        return True

input = sys.stdin.read()
data = list(map(int, input.split()))
n, m = data[0:2]
data = data[2:]
edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
adj = [[] for _ in range(n)]
balance = [0] * n
visited = [False] * n
for (a, b) in edges:
    adj[a - 1].append(b - 1)
    if a != b:
        balance[a-1] += 1
        balance[b-1] -= 1
if balanced(balance):
    visits = [len(i) for i in adj]
    print(1)
    print(*eulerian_cycle(visits,adj,edges))
else:
    print(0)
