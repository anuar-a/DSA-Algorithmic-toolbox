# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]
variables = []
clauses = []
for i in range(1,3*n+1,3):
    variables.append([i,i+1,i+2])

def printEquisatisfiableSatFormula(n,m,edges,variables):
    clauses = []
    clauses.append([3*m+n,3*n])
    for i in variables:
        clauses.append(i)
    for j in edges:
        clauses.append([-variables[j[0]-1][0],-variables[j[1]-1][0]])
        clauses.append([-variables[j[0]-1][1],-variables[j[1]-1][1]])
        clauses.append([-variables[j[0]-1][2],-variables[j[1]-1][2]])
    for k in range(1,len(clauses)):
        clauses[k].append(0)
    return clauses
answer = printEquisatisfiableSatFormula(n,m,edges,variables)
for line in answer:
    print(*line)
