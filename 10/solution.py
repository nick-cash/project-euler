from math import sqrt

limit = 2000000
cross_limit = int(sqrt(limit) - 1) / 2

sieve_bound = (limit - 1) / 2
sieve = [False for n in xrange(0, sieve_bound+1)]

for n in xrange(1, cross_limit):
    if not sieve[n]:
        for m in xrange(2*n*(n+1), sieve_bound, (2*n)+1):
            sieve[m] = True

print 2 + sum([(2*n) + 1 for n in xrange(1, sieve_bound) if not sieve[n]])
