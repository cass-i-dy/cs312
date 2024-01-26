# Fabonacci Series

def fib(n):
	if n <= 2:
		return 1
	return fib(n-1) + fib(n-2) + fib(n-3)

def fab(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	return fab(n-1) + fab(n-2)

def lin(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		curr = 1
		prev = 0
		for i in range(2, n+1):
			temp = curr
			curr = prev + curr
			prev = temp
		return curr

def fabonacci_exponential(n):
    if n <= 2:
        return 1
    else:
        return fabonacci_exponential(n-1) + fabonacci_exponential(n-2) * fabonacci_exponential(n-3)


def fabonacci_linear(n):
	if n <= 2:
		return 1

	result = 0
	adds = n - 2
	multiplies = n - 2

	a, b, c = 1, 1, 1

	for i in range(3, n + 1):
		result = b + a * c  # Addition and multiplication operations
		adds += 1
		multiplies += 1

		a = b
		b = c
		c = result

	return result, adds, multiplies


print(fabonacci_linear(9))