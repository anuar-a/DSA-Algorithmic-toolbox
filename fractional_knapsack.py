# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    for k,v in sorted(vperw.items(),key = lambda kv:(kv[1], kv[0]), reverse = True) :
        if capacity == 0:
            return value
        a = min(capacity,weights[int(k)])
        value = value + v*a
        weights[int(k)] = weights[int(k)] - a
        capacity = capacity - a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    vperw = dict()
    sorted_values = dict()
    for i in range(len(values)):
        vperw[i] = int(values[i])/int(weights[i])
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
