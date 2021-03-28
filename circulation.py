#python 3

import sys
from collections import defaultdict

#This class represents a directed graph using adjacency matrix representation
class Graph:

    def __init__(self,graph,edges):
        self.graph = graph # residual graph
        self.ROW = len(graph)
        self.edges = edges
        self.original = graph.copy()
        #self.COL = len(gr[0])


    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False]*(self.ROW)

        # Create a queue for BFS
        queue=[]

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

         # Standard BFS Loop
        while queue:

            #Dequeue a vertex from queue and print it
            #print(queue)
            u = queue.pop(0)
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        # If we reached sink in BFS starting from source, then return
        # true, else false
        #print(parent)
        return True if visited[t] else False


    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
        original = [x[:] for x in self.graph]
        max_flow = 0 # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow +=  path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
            #print('*****************')
            #for i in self.graph:
                #print(i)
            #print('*****************')
        answer = []
        #for i in self.graph:
            #print(i)
        for (u,v,bound) in edges:
            answer.append(bound+self.graph[v][u]-original[v][u])
            #print('Edge',u,v,bound,self.graph[v][u],original[v][u])
        if max_flow == sum(bounds):
            return answer
        else:
            return 'NO'


# Create a graph given in the above diagram
vertex_count, edge_count = map(int, input().split())
'''graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]'''
graph = [[0 for i in range(vertex_count+2)] for i in range(vertex_count+2)]
bounds = [0]*edge_count
edges = []
for _ in range(edge_count):
    u, v, bound, capacity = map(int, input().split())
    graph[u][v] = graph[u][v] + capacity - bound
    graph[u][vertex_count+1] += bound
    graph[0][v] += bound
    bounds[_] = bound
    edges.append((u,v,bound))
g = Graph(graph,edges)
#for i in g.graph:
    #print(i)
result = g.FordFulkerson(0, vertex_count+1)
if result == 'NO':
    print('NO')
else:
    print('YES')
    for i in result:
        print(i)
