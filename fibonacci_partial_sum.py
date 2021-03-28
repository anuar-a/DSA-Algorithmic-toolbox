# Uses python3

def fib_sum_last_digit(n):

    fib_numbers = [0,1]

    if n > 60 :
        for i in range(2,(n % 60) + 3):
            fib_numbers.append(int(fib_numbers[i-1]) + int(fib_numbers[i-2]))
        return ((fib_numbers[(n + 2) % 60] - 1) % 10)
    else:
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            for i in range(2,n + 3):
                fib_numbers.append(int(fib_numbers[i-1] % 10) + int(fib_numbers[i-2]) % 10)
            return(fib_numbers[n+2] - 1)

def fib_partial_sum(m, n):

    a = fib_sum_last_digit(m-1)
    b = fib_sum_last_digit(n)
    return (b-a) % 10

numbers = input()
m, n = numbers.split()
print(fib_partial_sum(int(m), int(n)))
