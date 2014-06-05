from math import sqrt

limit = 2000000
cross_limit = sqrt(limit)
sieve = [False for n in xrange(1, limit+1)]

# Construct our Eratosthenes sieve
for n in xrange(4, limit, 2):
    sieve[n] = True

for n in xrange(3, int(cross_limit), 2):
    if not sieve[n]:
        for m in xrange(n*n, limit, 2*n):
            if m > limit:
                print m
            sieve[m] = True

# Sum
total = 0
for n in xrange(2, limit):
    if not sieve[n]:
        total += n

print total
