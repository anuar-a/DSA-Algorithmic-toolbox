# python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

def main():
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]
    edges = []
    for clause in clauses:
        edges.append([-clause[0],clause[1]])
        edges.append([-clause[1],clause[0]])
    for i in range(len(edges)):
        for j in range(2):
            if edges[i][j] < 0:
                edges[i][j] = -edges[i][j] + n
    adj = [[] for _ in range(2*n)]
    adj_reversed = [[] for _ in range(2*n)]
    visited = [False] * 2*n
    post = [] * 2*n
    for i in edges:
        adj[i[0] - 1].append(i[1] - 1)
        adj_reversed[i[1] - 1].append(i[0] - 1)
    result = number_of_strongly_connected_components(adj,adj_reversed,n,visited,post)
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE");
        print(" ".join(str(i+1 if result[i] else -i-1) for i in range(n)))

def dfs(adj_reversed,visited,post):
    for i in range(len(adj_reversed)):
        if visited[i] == False:
            explore(i,adj_reversed,visited,post)
    return

def explore(v,adj_reversed,visited,post):
    visited[v] = True
    for i in adj_reversed[v]:
        if visited[i] == False:
            explore(i,adj_reversed,visited,post)
    post.append(v)
    return post

def number_of_strongly_connected_components(adj, adj_reversed,n,visited,post):
    count = 0
    answer = []
    table = [None]*2*n
    dfs(adj_reversed,visited,post)
    post1 = post.copy()
    post.clear()
    visited = [False] * 2*n
    scc = [0] * 2*n
    for i in reversed(post1):
        a = []
        if visited[i] == False:
                b = set(explore(i,adj,visited,a))
                if len(b) > 0:
                    answer.append(b)
                    count = count + 1
                    for literal in b:
                        scc[literal] = count
    for i in range(n):
        if scc[i] == scc[i+n]:
            return None
    for i in answer:
        for j in i:
            if table[j] == None:
                table[j] = 1
                if j > n-1:
                    table[j-n] = 0
                else:
                    table[j+n] = 0
    return table[:n]

# This is to avoid stack overflow issues
threading.Thread(target=main).start()
