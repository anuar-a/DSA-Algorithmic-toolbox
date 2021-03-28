# python3
from sys import stdin
from itertools import combinations,permutations

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, b, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    print('pV',pivot_element.row,pivot_element.column)
    print(a)
    if a[pivot_element.row][pivot_element.column] == 0:
        while a[pivot_element.row][pivot_element.column] == 0:
            if pivot_element.row == len(a)-1:
                return False
            else:
                pivot_element.row += 1
    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    a[pivot_element.row], b[pivot_element.row] = [x/a[pivot_element.row][pivot_element.column] for x in a[pivot_element.row]], b[pivot_element.row]/a[pivot_element.row][pivot_element.column]
    a[pivot_element.row][pivot_element.column] = 1
    #print(a)
    #print(b)
    for i in range(len(a)):
        if i != pivot_element.row:
            k = a[i][pivot_element.column]
            for j in range(len(a[i])):
                a[i][j] = a[i][j] - a[pivot_element.row][j] * k
            #a[i] = a[i] - a[pivot_element.row] * a[i][pivot_element.column]
            a[i][pivot_element.column] = 0
            b[i] = b[i] - b[pivot_element.row] * k
            #a[i] = [x - a[pivot_element.row]*a[i][pivot_element.column] for x in a[i]]     a[i] - a[pivot_element.row] * a[i][pivot_element.column]
    #print(a)
    #print(b)

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(n,m,A,b):
    ans = []
    combin = []
    z = [i for i in range(n+m+1)]
    for i in combinations(z,m):
        print(i)
        temp = []
        for j in i:
            temp.append(j)
        combin.append(temp)
    print(combin)
    aa = []
    BB = []
    for k in combin:
        print('--------------------',k)
        print(A)
        print(b)
        aa = []
        BB = []
        for j in k:
            aa.append(A[j])
            BB.append(b[j])
        size = len(aa)
        used_columns = [False] * size
        used_rows = [False] * size
        for step in range(size):
                print(aa)
                pivot_element = SelectPivotElement(aa, BB, used_rows, used_columns)
                if pivot_element == False:
                    print('sdasd')
                    ans.append([])
                else:
                    SwapLines(aa, BB, used_rows, pivot_element)
                    ProcessPivotElement(aa, BB, pivot_element)
                    MarkPivotElementUsed(pivot_element, used_rows, used_columns)
        ans.append(BB)
    #print(a)
        #print(b)
    return ans

def solve_diet_problem(n, m, A, b, c):
  # Write your code here

  print(SolveEquation(n,m,A,b))
  return [0, [0] * m]

if __name__ == "__main__":

    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
      A += [list(map(int, stdin.readline().split()))]
    b = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))
    for i in range(m):
        d = [0] * m
        d[i] = -1
        A.append(d)
        b.append(0)
    A.append([1]*m)
    b.append(10**9)
    A = tuple(A)
    b = tuple(b)
    print(A)
    print(b)
    anst, ansx = solve_diet_problem(n, m, A, b, c)
    if anst == -1:
      print("No solution")
    if anst == 0:
      print("Bounded solution")
      print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
    if anst == 1:
      print("Infinity")
