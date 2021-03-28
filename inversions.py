# Uses python3
import sys

def merge(a_array, b_array):
    global count
    d = []
    while len(a_array) != 0 and len(b_array) != 0:
        a = a_array[0]
        b = b_array[0]
        if a <= b:
            d.append(a_array[0])
            a_array.pop(0)
        else:
            d.append(b_array[0])
            b_array.pop(0)
            count = count + len(a_array)
    d = d + a_array + b_array
    a_array.clear()
    b_array.clear()
    return d

def get_number_of_inversions(a, b, left, right):
    global count
    number_of_inversions = 0
    a_sorted = []
    if right - left <= 1:
        return a[left:right]
    ave = (left + right) // 2
    a_array = get_number_of_inversions(a, b, left, ave)
    b_array = get_number_of_inversions(a, b, ave, right)
    a_sorted = merge(a_array, b_array)
    return a_sorted

if __name__ == '__main__':
    count = 0
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    get_number_of_inversions(a, b, 0, len(a))
    print(count)
