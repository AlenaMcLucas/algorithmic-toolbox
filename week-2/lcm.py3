import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_new(a, b):

	a_save = a
	b_save = b

	while b != 0:
		old_b = b
		b = a % b
		a = old_b
	
	return int((a_save * b_save) // a)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_new(a, b))

