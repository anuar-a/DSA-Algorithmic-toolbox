# Uses python3

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def lcm(a, b):
    x = (a*b)//gcd(a,b)
    return x

numbers = input()
a, b = numbers.split()
print(lcm(int(a), int(b)))
