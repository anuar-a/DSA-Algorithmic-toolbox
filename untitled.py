import sys
from collections import deque

a = [0,1,2,3,4]
b = 0
def test():
    global b
    b = b + 1
    return b

ans = test()
print(ans)
if test() > 0:
    print(ans)
quit()
q = deque('12')
min = - sys.maxsize
max = sys.maxsize
a = [1,2,3]
b = []
print(a.index(a[1]))
parents = [4,-1,4,1,1]
tree = dict()
for i in list(enumerate(parents)):
    tree[i[0]] = []
print(tree)
for i in list(enumerate(parents)):
    if i[1] == -1:
        continue
    tree[i[1]].append(i[0])
print(tree)
q.append(a[0])
print(q)
print(len(q))
q.popleft()
print(q)
print(len(q))
q.pop()
print(q)
print(len(q))
if b == []:
    print('Empty')
