import random
def prime_test(N, k):
	return fermat(N,k), miller_rabin(N,k)

def mod_exp(x, y, N):
	if y == 0:
		return 1
	z = mod_exp(x, y//2, N)
	if y % 2 == 0:
		return z**2%N
	else:
		return x*z**2%N
	
def fprobability(k):
    return 1-.5**k

def mprobability(k):
    return 1-.25**k
def fermat(N,k):
	a_vals = [random.randint(1,N) for i in range(k)]
	for a in a_vals:
		if mod_exp(a,N-1,N) != 1:
			return 'composite'
	return 'prime'
def miller_rabin_helper(a, N, mod):
	if N%2 != 0:
		return 'prime'
	ans = mod_exp(a,N,mod)
	if (ans == -1) or (ans == (mod - 1)):
		return 'prime'
	elif ans != 1:
		return 'composite'
	else:
		miller_rabin_helper(a, N//2, mod)

def miller_rabin(N,k):
	a_vals = [random.randint(1, k) for i in range(k)]
	for a in a_vals:
		if N % 2 == 0:
			return 'composite'
		if miller_rabin_helper(a,N-1,N) == 'composite':
			return 'composite'
	return 'prime'

if __name__ == '__main__':
    print(fermat(79,3))