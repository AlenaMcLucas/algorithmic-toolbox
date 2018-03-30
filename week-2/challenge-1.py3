def calc_fib(n):

	fibonacci = [0,1]
	counter = 2

	while counter <= n:
		fibonacci.append(fibonacci[counter - 1] + fibonacci[counter - 2])
		counter += 1

	return fibonacci[n]

n = int(input())
print(calc_fib(n))
