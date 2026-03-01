def factorial(n):
	if n < 0:
        	return
	if n == 0 or n == 1:
        	return 1
	res = n * factorial(n - 1)
		return res
def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def fibonacci(n):
    if n <= 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
def is_even(n):
    return n % 2 == 0
def is_palindrome(text):
    s = str(text).lower().replace(" ", "")
    return s == s[::-1]
