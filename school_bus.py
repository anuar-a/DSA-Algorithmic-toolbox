# python3
from itertools import permutations,combinations
INF = 10 ** 9

def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph

def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))

def convert(tup):
    ans = 0
    for i in tup:
        ans = ans + 2**i
    return ans

def optimal_path(graph):
    # This solution tries all the possible sequences of stops.
    # It is too slow to pass the problem.
    # Implement a more efficient algorithm here.
    n = len(graph)
    C = [[INF]*n for i in range(2**n-1)]
    print(C)
    C[1][0] = 0
    for s in range(2,n+1):
        for c in combinations(set(range(n)),s):
            if 0 in c:
                print(c,convert(c))
                C[convert(c)][0] = INF
                for i in c:
                    if i != 0:
                        for j in c:
                            if j!= i:
                                print(i,j)
                                print(C[convert(c)][i])
                                print(convert(c)^1<<j)
                                C[convert(c)][i] = min(C[convert(c)][i],C[convert(c)^(1<<i)][j] + graph[i][j])
    best_ans = INF
    best_path = []
    for i in range(n):
        best_ans = min(best_ans,C[2**n-1][i] + graph[i][0])
    if best_ans == INF:
        return(-1,[])
    return (best_ans, [x + 1 for x in best_path])
    '''n = len(graph)
    best_ans = INF
    best_path = []

    for p in permutations(range(n)):
        cur_sum = 0
        for i in range(1, n):
            if graph[p[i - 1]][p[i]] == INF:
                break
            cur_sum += graph[p[i - 1]][p[i]]
        else:
            if graph[p[-1]][p[0]] == INF:
                continue
            cur_sum += graph[p[-1]][p[0]]
            if cur_sum < best_ans:
                best_ans = cur_sum
                best_path = list(p)

    if best_ans == INF:
        return (-1, [])
    return (best_ans, [x + 1 for x in best_path])'''


if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
