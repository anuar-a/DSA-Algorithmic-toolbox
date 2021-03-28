#python3
import sys

def eulerian_cycle(adj):
    edge_count = dict()
    curr_path = []
    circuit = str()
    for i in adj.keys():
        edge_count[i] = len(adj[i])
    curr_path.append(list(adj.keys())[0])
    curr_v = list(adj.keys())[0]
    while len(curr_path) > 0:
        if edge_count[curr_v] > 0:
            curr_path.append(curr_v)
            next_v = adj[curr_v][-1]
            edge_count[curr_v] -= 1
            adj[curr_v].pop()
            curr_v = next_v
        else:
            circuit = circuit + curr_v[-1]
            curr_v = curr_path[-1]
            curr_path.pop()
    return circuit[::-1]


k = int(input())
edges = []
adj = dict()
reads = []
for i in range(2**k):
    reads.append(format(i, '0' + str(k) + 'b'))
for i in range(2**(k-1)):
    adj[format(i,'0' + str((k-1)) + 'b')] = []
for read in reads:
    adj[read[:-1]].append(read[1:])
print(eulerian_cycle(adj)[:-1])
