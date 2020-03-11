import math

def is_palindrome(n):
	length = countDigit(n)
	for x in range(0,length//2):
		num1=n//10**(length-x-1) % 10
		num2=n//10**x % 10
		if num1 != num2:
			return False
	return True

def countDigit(n):
    count = 0
    while n != 0: 
        n //= 10
        count+= 1
    return count

print is_palindrome(1234321)
# True
print is_palindrome(1234432)
# False