# python3

import sys
from itertools import permutations, combinations

squares = list(sys.stdin.read().split())
n = int(len(squares) ** 0.5)
for i in range(len(squares)):
    squares[i] = squares[i][1:-1]
    squares[i] = tuple(squares[i].split(","))
answer = [[0] * n for i in range(n)]
final_answer = [[0] * n for i in range(n)]
seta = set()
setb = set()
setc = set()
setd = set()
set1 = set()
set2 = set()
set3 = set()

for (a,b,c,d) in squares:
    if a == 'black' and b == 'black':
        answer[0][0] = (a,b,c,d)
    if a == 'black' and d == 'black':
        answer[0][n-1] = (a,b,c,d)
    if b == 'black' and c == 'black':
        answer[n-1][0] = (a,b,c,d)
    if c == 'black' and d == 'black':
        answer[n-1][n-1] = (a,b,c,d)
for (a,b,c,d) in squares:
    if a == 'black' and (b != 'black' and d != 'black'):
        seta.add((a,b,c,d))
    if b == 'black' and (a != 'black' and c != 'black'):
        setb.add((a,b,c,d))
    if c == 'black' and (b != 'black' and d != 'black'):
        setc.add((a,b,c,d))
    if d == 'black' and (a != 'black' and c != 'black'):
        setd.add((a,b,c,d))

for i in permutations(seta):
    if i[0][1] == answer[0][0][3] and i[0][3] == i[1][1] and i[1][3] == i[2][1] and i[2][3] == answer[0][4][1]:
        answer[0][1] = i[0]
        answer[0][2] = i[1]
        answer[0][3] = i[2]
for i in permutations(setb):
    if i[0][0] == answer[0][0][2] and i[0][2] == i[1][0] and i[1][2] == i[2][0] and i[2][2] == answer[4][0][0]:
        answer[1][0] = i[0]
        answer[2][0] = i[1]
        answer[3][0] = i[2]
for i in permutations(setc):
    if i[0][1] == answer[4][0][3] and i[0][3] == i[1][1] and i[1][3] == i[2][1] and i[2][3] == answer[4][4][1]:
        answer[4][1] = i[0]
        answer[4][2] = i[1]
        answer[4][3] = i[2]
for i in permutations(setd):
    if i[0][0] == answer[0][4][2] and i[0][2] == i[1][0] and i[1][2] == i[2][0] and i[2][2] == answer[4][4][0]:
        answer[1][4] = i[0]
        answer[2][4] = i[1]
        answer[3][4] = i[2]
for (a,b,c,d) in squares:
    if a == answer[0][1][2] and b == answer[1][0][3]:
        answer[1][1] = (a,b,c,d)
    if a == answer[0][3][2] and d == answer[1][4][1]:
        answer[1][3] = (a,b,c,d)
    if b == answer[3][0][3] and c == answer[4][1][0]:
        answer[3][1] = (a,b,c,d)
    if c == answer[4][3][0] and d == answer[3][4][1]:
        answer[3][3] = (a,b,c,d)
for (a,b,c,d) in squares:
    if a == answer[0][2][2] and b == answer[1][1][3] and d == answer[1][3][1]:
        answer[1][2] = (a,b,c,d)
    if a == answer[1][1][2] and b == answer[2][0][3] and c == answer[3][1][0]:
        answer[2][1] = (a,b,c,d)
    if a == answer[1][3][2] and c == answer[3][3][0] and d == answer[2][4][1]:
        answer[2][3] = (a,b,c,d)
    if b == answer[3][1][3] and c == answer[4][2][0] and d == answer[3][3][1]:
        answer[3][2] = (a,b,c,d)
for (a,b,c,d) in squares:
    if a == answer[1][2][2] and b == answer[2][1][3] and c == answer[3][2][0] and d == answer[2][3][1]:
        answer[2][2] = (a,b,c,d)
for i in range(5):
    for j in range(5):
        final_answer[i][j] = '(' + answer[i][j][0] + ',' + answer[i][j][1] + ',' + answer[i][j][2] + ',' + answer[i][j][3] + ')'
for line in final_answer:
    print(line[0]+';'+line[1]+';'+line[2]+';'+line[3]+';'+line[4])
