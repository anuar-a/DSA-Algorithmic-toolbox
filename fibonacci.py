# Uses python3

def calc_fib(n):
    fib_numbers = ["0","1"]
    for i in range(2,n+1):
            fib_numbers.append(int(fib_numbers[i-1])+int(fib_numbers[i-2]))

    return fib_numbers[n]

n = int(input())
print(calc_fib(n))
