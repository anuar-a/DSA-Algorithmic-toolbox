#Uses python3
import sys
import math

def distance(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def merge(a_array, b_array):
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
    d = d + a_array + b_array
    return d

def minimum_split(b,border,d):
    #print(b)
    left = []
    right = []
    #print(b)
    for i in b:
        if abs(i[0] - border) <= d:
            right.append(i)
    #print(right)
    #total = left + right
    #total.sort(key = lambda x:x[1])
    #print('Total',total)
    result = d
    #print('Result',result)
    for i in range(len(right)):
        for j in range(i + 1, min(i+8, len(right))):
            result = min(result, distance(right[i], right[j]))
    #print('Result',result)
    return result

def minimum_distance(a,b,x):
    #write your code here
    min_dist = sys.maxsize
    if len(a) <= 3:
        for i in range(0,len(a)):
            for j in range(i+1,len(a)):
                min_dist = min(min_dist, distance(a[i],a[j]))
        return min_dist
    mid = len(a) // 2
    #print(mid)
    left_points = a[:mid]
    right_points = a[mid:]
    left_points_x = x[:mid]
    right_points_x = x[mid:]
    left_min = minimum_distance(left_points,b,left_points_x)
    right_min = minimum_distance(right_points,b,right_points_x)
    border = (left_points_x[len(left_points_x)-1] + right_points_x[0])/2
    normal_min = min(left_min,right_min)
    #print(mid,border)
    #print('Normal',normal_min)
    #print('B is',b)
    split_min = minimum_split(b,border,normal_min)
    return min(left_min,right_min,split_min)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    '''input = open("test.txt")
    data = list()
    for i in input:
        data.append(int(i))'''
    a = list()
    b = list()
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    for i in range(0,n):
        a.append((x[i],y[i]))
    #print(data)
    a.sort()
    x.sort()
    b = sorted(a,key = lambda x:x[1])
    #print(a)
    #print(b)
    print("{0:.4f}".format(minimum_distance(a,b,x)))
