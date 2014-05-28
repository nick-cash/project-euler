# This could be any of dozens of primality checking algorithms
def prime(a):
    return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

num_primes = 0
num = 1

while num_primes < 10001:
    num += 1

    if prime(num):
        num_primes += 1

print num
