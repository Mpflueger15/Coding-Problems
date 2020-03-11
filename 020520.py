def find_primes(n):
	composite = []
	for num in range(2, n):
		for div in range(2,n):
			if num > div and num%div==0:
				composite.append(num)
	primes = [x for x in range(2,n) if x not in composite]
	return primes

print(find_primes(50))
# [2, 3, 5, 7, 11, 13]
