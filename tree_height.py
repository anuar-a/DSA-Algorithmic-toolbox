# python3

import sys
import threading
from collections import deque

def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 1
    tree = dict()
    q = deque()
    h = deque([1])
    #print(h)
    count = 0
    root = parents.index(-1)
    #print(root)
    for i in list(enumerate(parents)):
        tree[i[0]] = []
    for i in list(enumerate(parents)):
        if i[1] == -1:
            continue
        tree[i[1]].append(i[0])
    #print(tree)
    q.append(root)
    while len(q) > 0:
        #print(q)
        node = q.popleft()
        current = h.popleft()
        max_height = max(max_height,current)
        #print(node)
        for i in tree[node]:
            q.append(i)
            count = count + 1
            h.append(current+1)
        #print(h)
#    print(count)
#    for i in list(enumerate(parents)):
#        dict[i] = i[0]
    '''for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)'''
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
