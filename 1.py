#python

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

a = 'ABCDEF'
b = 'CDE'
print(overlap(a,b))
