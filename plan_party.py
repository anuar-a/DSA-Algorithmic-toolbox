#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, v, parent, D):
    if D[v] == float('inf'):
        if len(tree[v].children) == 1 and v != 0:
            D[v] = tree[v].weight
        else:
            m_1 = tree[v].weight
            for u in tree[v].children:
                if parent != u:
                    for w in tree[u].children:
                        if w != v:
                            m_1 = m_1 + dfs(tree,w,u,D)
            m_0 = 0
            for u in tree[v].children:
                if u != parent:
                    m_0 = m_0 + dfs(tree,u,v,D)
            D[v] = max(m_1,m_0)
    return D[v]

def MaxWeightIndependentTreeSubset(tree):
    D = [float('inf')] * len(tree)
    answer = dfs(tree, 0, -1, D)
    return answer


def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
