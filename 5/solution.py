import operator
from collections import OrderedDict

primes = OrderedDict()
for line in open('primes.txt'):
    for prime in line.split():
        primes[int(prime)] = 0

for n in xrange(2, 21):
    for prime in primes:
        if (n % prime) == 0:
            exp = 1

            while (n % (prime ** (exp+1))) == 0:
                exp += 1

            primes[prime] = max(exp, primes[prime])
            n /= (prime ** exp)

print primes
print reduce(operator.mul,
             [(prime ** exponent) for prime, exponent in primes.iteritems()],
             1)
