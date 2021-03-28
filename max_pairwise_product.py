# python3
n = 2*10**5
print(n)
a = [int(x) for x in range(2*10**5)]
max_index1 = -1
max_index2 = -1
product = 0

for i in range(n):
    if max_index1 == -1 or a[i] > a[max_index1]:
        max_index1 = i

for j in range(n):
    if j != max_index1 or max_index2 == -1 or a[i] > a[max_index2]:
        max_index2 = j

print(a[max_index1] * a[max_index2])
