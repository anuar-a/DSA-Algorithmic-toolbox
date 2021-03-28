#Uses python3

import sys

def dfs(adj,clk):
    #cc = 0
    for i in range(len(adj)):
        if visited[i] == False:
            explore(i,adj,clk)
            #cc = cc + 1
    return post

def explore(v,adj,clk):
    visited[v] = True
    for i in adj[v]:
        if visited[i] == False:
            explore(i,adj,clk)
    post.append(v)
    return visited

def acyclic(adj):
    clk = 0
    dfs(adj,clk)
    post1 = [0] * n
    for i in reversed(post):
        post1[i] = post.index(i)
    for (a, b) in edges:
        if post1[a-1] <= post1[b-1]:
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    visited = [False] * n
    post = [] * n
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
