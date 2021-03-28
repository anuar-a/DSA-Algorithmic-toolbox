# Uses python3
import sys

def get_majority_element(a, left, right):
    #print(a[left:right])
    if len(a[left:right]) == 1:
        #print('Unit is',a[left])
        return a[left]
    k = (right + left) // 2
    lmajor = get_majority_element(a,left,k)
    rmajor = get_majority_element(a,k,right)
    if lmajor == rmajor:
        #print('Equal are',lmajor,rmajor)
        return lmajor
    lcount = 0
    rcount = 0
    #print('Different are',a[left:right])
    for i in a[left:right]:
        if i == lmajor:
            lcount = lcount + 1
        if i == rmajor:
            rcount = rcount + 1
    #print(a[left:right],'has counts',lcount,rcount)
    if lcount > len(a[left:right])//2 :
        return lmajor
    if rcount > len(a[left:right])//2 :
        return rmajor
    #print('No majority in',a[left:right])
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
