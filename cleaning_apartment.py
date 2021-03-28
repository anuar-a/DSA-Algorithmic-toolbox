# python3
from itertools import combinations

n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]
variables = []
clauses = []
for i in range(1,n*n+1,n):
    temp = []
    for j in range(n):
        temp.append(i+j)
    variables.append(temp)
#for line in variables:
    #print(line)

def printEquisatisfiableSatFormula(n,m,edges,variables):
    edges_set = set()
    for i in edges:
        edges_set.add((i[0],i[1]))
        edges_set.add((i[1],i[0]))
    clauses = []
    clauses.append([0,n*n])
    for i in variables:
        clauses.append(i)
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(variables[j][i])
        clauses.append(temp)
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(-variables[j][i])
        for k in combinations(temp,2):
            clauses.append(list(k))
    '''for i in variables:
        for j in combinations(i,2):
            clauses.append(list(j))'''
    for i in combinations(range(1,n+1),2):
        if i not in edges_set:
            #print('sdasd',i)
            for j in variables[i[0]-1]:
                for k in variables[i[1]-1]:
                    if abs(j-(i[0]-1)*n-k+(i[1]-1)*n) == 1:
                        clauses.append([-j,-k])
    for k in range(1,len(clauses)):
        clauses[k].append(0)
    clauses[0][0] = len(clauses)-1

    return clauses

answer = printEquisatisfiableSatFormula(n,m,edges,variables)
for line in answer:
    print(*line)
