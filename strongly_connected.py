#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs(adj_reversed):
    for i in range(len(adj_reversed)):
        if visited[i] == False:
            explore(i,adj_reversed,visited)
    return

def explore(v,adj_reversed,visited):
    visited[v] = True
    for i in adj_reversed[v]:
        if visited[i] == False:
            explore(i,adj_reversed,visited)
    post.append(v)
    return visited

def number_of_strongly_connected_components(adj, adj_reversed):
    count = 0
    dfs(adj_reversed)
    post1 = post.copy()
    post.clear()
    visited = [False] * n
    for i in reversed(post1):
        result = visited.copy()
        if visited[i] == False:
            if result != explore(i,adj,visited):
                count = count + 1
    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_reversed = [[] for _ in range(n)]
    visited = [False] * n
    post = [] * n
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    for (b, a) in edges:
        adj_reversed[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj, adj_reversed))
