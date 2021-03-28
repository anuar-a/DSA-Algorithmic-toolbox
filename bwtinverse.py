# python3
import sys

def InverseBWT(bwt):
    # write your code here
    result = str()
    #temp = sorted(bwt)
    #bwt_sorted = ''.join(temp)
    #print(bwt)
    #print(temp)
    #print(bwt_sorted)
    #str1 = [(1,'$')]
    str2 = []
    a_count1 = 0
    c_count1 = 0
    g_count1 = 0
    t_count1 = 0
    a_count2 = 0
    c_count2 = 0
    g_count2 = 0
    t_count2 = 0
    for i in range(len(bwt)):
        if bwt[i] == 'A':
            a_count2 = a_count2 + 1
            str2.append((a_count2,'A'))
        if bwt[i] == 'C':
            c_count2 = c_count2 + 1
            str2.append((c_count2,'C'))
        if bwt[i] == 'G':
            g_count2 = g_count2 + 1
            str2.append((g_count2,'G'))
        if bwt[i] == 'T':
            t_count2 = t_count2 + 1
            str2.append((t_count2,'T'))
        '''if bwt_sorted[i] == 'A':
            a_count2 = a_count2 + 1
            str1.append((a_count2,'A'))
        if bwt_sorted[i] == 'C':
            c_count2 = c_count2 + 1
            str1.append((c_count2,'C'))
        if bwt_sorted[i] == 'G':
            g_count2 = g_count2 + 1
            str1.append((g_count2,'G'))
        if bwt_sorted[i] == 'T':
            t_count2 = t_count2 + 1
            str1.append((t_count2,'T'))'''
        if bwt[i] == '$':
            str2.append((1,'$'))
    #print(str1)
    #print(str2)
    elem = (0,'$')
    for i in range(len(bwt)):
        ind = 0
        result = result + str(elem[1])
        #print(result)
        if elem[1] == '$':
            ind = 0
        if elem[1] == 'A':
            ind = elem[0]
        if elem[1] == 'C':
            ind = elem[0] + a_count2
        if elem[1] == 'G':
            ind = elem[0] + a_count2 + c_count2
        if elem[1] == 'T':
            ind = elem[0] + a_count2 + c_count2 + g_count2
        #ind = str1.index(elem)
        elem = str2[ind]

    return result[::-1]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
