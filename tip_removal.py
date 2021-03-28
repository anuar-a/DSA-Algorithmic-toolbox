#python 3

import sys

sys.setrecursionlimit(10**7)

def dfs(adj_reversed):
    for i in adj_reversed:
        if visited[i] == False:
            explore(i,adj_reversed,visited)
    return

def explore(v,adj_reversed,visited):
    #print(v)
    flag = False
    visited[v] = True
    if v in adj_reversed:
        for i in adj_reversed[v]:
            if visited[i] == False:
                flag = True
                explore(i,adj_reversed,visited)

    post.append(v)
    #ans.append(v)
    #print(ans)
    return visited, flag

def number_of_strongly_connected_components(adj, adj_reversed,nodes,visited):
    count = 0
    dfs(adj_reversed)
    post1 = post.copy()
    post.clear()
    visited = dict()
    visited.fromkeys(nodes)
    for i in nodes:
        visited[i] = False
    for i in reversed(post1):
        result = visited.copy()
        if visited[i] == False:
            arr,flag = explore(i,adj,visited)
            #if list(result.values()).count(False) - list(arr.values()).count(False) == 1:
            if not flag:
                count = count + 1
    return count

k = 15
reads = list(sys.stdin.read().strip().split())
adj = dict()
adj_reversed = dict()
reads_k = list()
nodes = set()
for read in reads:
    for i in range(len(read)-k+1):
        reads_k.append(read[i:i+k])
for read in reads_k:
    adj[read[:-1]] = set()
    adj_reversed[read[1:]] = set()
    nodes.add(read[1:])
    nodes.add(read[:-1])
for read in reads_k:
    if read[:-1] != read[1:]:
        adj[read[:-1]].add(read[1:])
        adj_reversed[read[1:]].add(read[:-1])
visited = dict()
visited.fromkeys(nodes)
for i in nodes:
    visited[i] = False
post = [] * len(nodes)
#print(adj)
#print(adj_reversed)
#print(nodes)
print(number_of_strongly_connected_components(adj, adj_reversed, nodes, visited))
