# Uses python3

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

numbers = input()
a, b = numbers.split()
print(gcd(int(a), int(b)))
