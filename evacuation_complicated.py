# python3

import sys
from collections import deque

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = capacity

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def group(self):
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])-1):
                for k in range(j+1,len(self.graph[i])):
                    if self.edges[self.graph[i][j]].u == self.edges[self.graph[i][k]].u and self.edges[self.graph[i][j]].v == self.edges[self.graph[i][k]].v:
                        self.edges[self.graph[i][j]].capacity = self.edges[self.graph[i][j]].capacity + self.edges[self.graph[i][k]].capacity
                        self.edges[self.graph[i][j]].flow = self.edges[self.graph[i][j]].flow + self.edges[self.graph[i][k]].flow
                        self.graph[i].remove(k)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


    def distance(self, s, t, parent):
        #write your code here
        dist = [0] * len(self.graph)
        prev = [0] * len(self.graph)
        visited = [False] * len(self.graph)
        for i in range(len(self.graph)):
            dist[i] = sys.maxsize
            prev[i] = 0
        dist[s] = 0
        visited[s] = True
        q = deque([s])
        while len(q) > 0:
            u = q.popleft()
            for i in self.graph[u]:
                if i % 2 == 0:
                    if visited[self.edges[i].v] == False and self.edges[i].flow > 0:
                        q.append(self.edges[i].v)
                        dist[self.edges[i].v] = dist[u] + 1
                        visited[self.edges[i].v] = True
                        prev[self.edges[i].v] = u
                        parent[self.edges[i].v] = u

        if visited[t]:
            return True
        else:
            return False
        '''if dist[t] == sys.maxsize:
            return -1
        else:
            return dist[t]'''
        '''result = []
        u = t
        while u != s:
            result.append(u)
            u = prev[u]
        print(result)
        return result'''

    def max_flow(self, from_, to):
        flow = 0
        # your code goes here
        parent = [-1] * len(self.graph)
        max_flow = 0
        while self.distance(from_, to, parent):
            path_flow = float('Inf')
            s = to
            while s != from_:
                for i in self.get_ids(s):
                    if self.edges[i^1].u == parent[s] and self.edges[i^1].v == s:
                        path_flow = min(path_flow,self.edges[i^1].capacity)
                        s = parent[s]
                        #break
            max_flow = max_flow + path_flow
            print(max_flow)
            v = to
            while v != from_:
                for i in self.get_ids(v):
                    if self.edges[i^1].u == parent[v] and self.edges[i^1].v == v:
                        u = parent[v]
                        self.add_flow(i,path_flow)
                v = parent[v]
            print(parent)
            #quit()
        return max_flow

        #return flow

def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph





if __name__ == '__main__':
    graph = read_data()
    print(graph.graph)
    for i in graph.edges:
        print(i.u,i.v,i.capacity,i.flow)
    print(graph.max_flow(0, graph.size() - 1))
