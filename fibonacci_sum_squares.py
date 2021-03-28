# Uses python3

def fib_huge(n):

    fib_numbers = [0,1]
    fib_numbers_rem = [0,1]
    period = 0

    for i in range(2,n+1):
        fib_numbers.append(int(fib_numbers[i-1])+int(fib_numbers[i-2]))
        fib_numbers_rem.append((int(fib_numbers_rem[i-1]) % 10 + int(fib_numbers_rem[i-2])) % 10)
        if fib_numbers_rem[i] == 1 and fib_numbers_rem[i-1] == 0:
            period = i-1
            break
        else:
            continue

    if period == 0 : return fib_numbers_rem[n]
    else : return fib_numbers_rem[n % period]

def fib_sum_squares(n):

    return ((fib_huge(n) * fib_huge(n+1)) % 10 )

n = input()
print(fib_sum_squares(int(n)))
