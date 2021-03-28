#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    while len(a) != 0:
        maxDigit = 0
        for number in a:
            if int(str(number) + str(maxDigit)) >= int(str(maxDigit) + str(number)):
                maxDigit = number
        res = res + (str(maxDigit))
        a.remove(maxDigit)

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
