import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    fibonacci = [0,1]
    counter = 2

    while counter <= n:
        fibonacci.append(int(str(fibonacci[counter - 1] + fibonacci[counter - 2])[-1]))
        counter += 1

    return fibonacci[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
