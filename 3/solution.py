primes = []
for line in open('primes.txt'):
    primes.extend(line.split())

for prime in reversed(primes):
    if (600851475143 % int(prime)) == 0:
        print prime
        break
