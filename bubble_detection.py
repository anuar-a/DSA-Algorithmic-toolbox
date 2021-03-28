#python 3

import sys,time
from timeit import default_timer as timer
#sys.setrecursionlimit(10**7)

def compare_paths(a,b):
    #flag = 0
    #print(paths[i])
    #print(paths[j])
    #print(a)
    a_keys_dict = set(a)
    for i in b:
        if i in a_keys_dict:
            return 0
    return 1
    '''for k in a:
        for l in b:
            if k != a[0] and k != a[-1] and l != b[0] and b[-1]:
                if k == l:
                    return 0
    return 1'''
        #print('sdasd')

def find_bubbles(paths,t):
    counts = 0
    #print(paths)
    #start = timer()
    if len(paths) > 1:
        for i in range(len(paths)-1):
            a_keys_dict = set(paths[i][1:-1])
            for j in range(i+1,len(paths)):
                if len(paths[i])-1 <= t and len(paths[j])-1 <= t:
                    cnt = 1
                    for k in paths[j][1:-1]:
                        if k in a_keys_dict:
                            cnt = 0
                            break
                    #start = timer()
                    counts += cnt
                    #counts += compare_paths(paths[i][1:-1],paths[j][1:-1])
                    #end = timer()
                    #print(1000*(end-start))
    #end = timer()
    #print(end-start)
    return counts

def dfs(start,stop,adj,visited):
    #start = timer()
    path = []
    answer = []
    #for i in visited.keys():
    #    visited[i] = False
    explore(start,stop,adj,visited,path,answer,t)
    #end = timer()
    #print(end-start)
    return answer

def explore(u,v,adj,visited,path,answer,t):
    visited[u] = True
    path.append(u)
    if u == v:
        if len(path)-1 <= t:
            pth = path[:]
            answer.append(pth)
    else:
        if u in adj.keys():
        #try:
            for i in adj[u]:
                if visited[i] == False:
                    explore(i,v,adj,visited,path,answer,t)
        #except:
            #pass
    path.pop()
    visited[u] = False


k, t = map(int,sys.stdin.readline().split())
adj = dict()
reads = list(sys.stdin.read().strip().split())
in_set = set()
reads_k = list()
n = len(reads[0])
in_edges = []
out_edges = []
visited = dict()
post = []
#start = timer()
for read in reads:
    for i in range(len(read)-k+1):
        reads_k.append(read[i:i+k])
for read in reads_k:
    adj[read[:-1]] = set()
    in_set.add(read[:-1])
    in_set.add(read[1:])
for read in reads_k:
    if read[:-1] != read[1:]:
        adj[read[:-1]].add(read[1:])
for i in adj.keys():
    if len(adj[i]) > 1:
        out_edges.append(i)
#for i in adj.values():
#    in_set.update(i)
for i in in_set:
    visited[i] = False
    count = 0
    for j in adj.values():
        if i in j:
            count += 1
    if count > 1:
        in_edges.append(i)
count = 0
#end = timer()
#print((end-start)*1000)
#start = timer()
time = 0
for i in out_edges:
    for j in in_edges:
        if i != j:
            #print(i,j)
            #start = timer()
            count = count + find_bubbles(dfs(i,j,adj,visited),t)
            #end = timer()
            #print(1000*(end-start))
            #time += (end - start)
#end = timer()
#print((end-start)*1000)
#print(time*1000)
print(count,end='')
