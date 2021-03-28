# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
#print('Lines',lines)
#rank = [1] * n
rank = lines.copy()
#print('Rank',rank)
parent = list(range(0, n))
answer = max(lines)
#print('Parent',parent)

def ans(lines):
    return max(lines)

def Find(table):
    # find parent and compress path
    if table != parent[table]:
        parent[table] = Find(parent[table])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = Find(destination), Find(source)
    global answer
    if realDestination == realSource:
        return
    '''if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination
        lines[realSource] = lines[realSource] + rank[realDestination]
    else:'''
    parent[realSource] = realDestination
    lines[realDestination] = lines[realDestination] + lines[realSource]
    if lines[realDestination] > answer:
        answer = lines[realDestination]
    '''    if rank[realDestination] == rank[realSource]:
            rank[realSource] = rank[realSource] + 1'''
    # merge two components
    # use union by rank heuristic
    # update ans with the new maximum table size

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(answer)
#print('Rank',rank)
#print('Parent',parent)
#print('Lines',lines)
