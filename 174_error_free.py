#python3

import sys

def find_overlap(a,b):
    for i in range(100):
        k = i
        j = 0
        while k < 100:
            if a[k] != b[j]:
                break
            j += 1
            k += 1
        if k == 100:
            return 100 - i
    return 0

def overlap(a,b):
    #a = a[1:]
    i = 0
    j = 0
    while (i < len(a) and j < len(b)):
        if a[i] == b[j]:
            while (i < len(a) and j < len(b)) and a[i] == b[j]:
                i += 1
                j += 1
            break
        i += 1

    return j

def find_genome(reads):
    n = len(reads)
    genome = str(reads[0])
    visited = set('0')
    cur_read = 0

    while len(visited) != n:
        max_overlap = 0
        next_read = -1

        for i in range(n):
            if i not in visited:
                overlap = find_overlap(reads[cur_read],reads[i])
                if overlap > max_overlap:
                    max_overlap = overlap
                    next_read = i

        genome = genome + reads[next_read][find_overlap(reads[cur_read],reads[next_read]):]
        cur_read = next_read
        visited.add(cur_read)
    genome = genome[find_overlap(reads[cur_read],reads[0]):]
    return genome.strip()


reads = list(set(sys.stdin.read().strip().split()))
n = len(reads)
print(find_genome(reads),end='')
