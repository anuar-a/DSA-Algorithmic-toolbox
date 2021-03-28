#python3
import sys

def overlap(a,b):
    #a = a[1:]
    i = 1
    j = 0
    k = 0
    while (i < len(a) and j < len(b)):
        if a[i] == b[j]:
            while (i < len(a) and j < len(b)) and a[i] == b[j]:
                i += 1
                j += 1
                k += 1
            break
        i += 1

    return j

reads = list(set(sys.stdin.read().strip().split()))
#print(reads)
n = len(reads)
overlap_table = [[0]*n for i in range(n)]
overlap_dict = dict()
for i in range(n):
    for j in range(n):
        if i != j:
            overlap_table[i][j] = overlap(reads[i],reads[j])
#print(reads)
#for i in overlap_table:
    #print(i)
max_i = 0
max_j = 0
for i in range(n):
    max_ind = 0
    for j in range(n):
        if i != j and overlap_table[i][j] > overlap_table[i][max_ind]:
            max_ind = j
    overlap_dict[reads[i]] = reads[max_ind]
    if overlap_table[i][max_ind] > overlap_table[max_i][max_j]:
        max_i = i
        max_j = max_ind
    #print(max_i,max_j)
#print(overlap_dict)
visited = dict()
for read in reads:
    visited[read] = False
path = [reads[max_i]]
visited[reads[max_i]] = True
while True:
    #if not visited[overlap_dict[path[-1]]]:
    path.append(overlap_dict[path[-1]])
    visited[overlap_dict[path[-1]]] = True
    if len(path) == n:
        break
#print(path)
genome = str(path[0])
for i in range(1,len(path)):
    genome.strip()
    genome = genome + path[i][overlap(path[i-1],path[i]):]
    genome.strip()
#print(genome)
#print(genome[:2])
#print(genome[-2:])
cut = overlap(path[-1],path[0])
'''if genome[0] == genome[-1]:
    #print('asd')
    cut = 1
    while genome[:cut+1] == genome[-cut-1:]:
        cut += 1'''
if cut > 0:
    genome = genome[:-cut]
genome.strip()
#print(len(genome))
print(genome)
