# Uses python3
import sys
from operator import itemgetter

def get_optimal_value(capacity, weights, values):
    value = 0.
    items = []

    # create 3d list to store info in
    for i in range(len(weights)):
    	items.extend([[values[i],weights[i],(float(values[i])/float(weights[i]))]])
    
    #sort items my maximum value per weight unit
    items = sorted(items, key = itemgetter(2), reverse = True)
    #print(items)

    while capacity > 0 and items != []:
        if items[0][1] < capacity:
            current_item = items.pop(0)
            value += current_item[0]
            capacity -= current_item[1]
        else:
            current_item = items.pop(0)
            value += (capacity/current_item[1])*current_item[0]
            capacity = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
