valid = lambda x: (x % 3) == 0 or (x % 5) == 0
print sum([num if valid(num) else 0 for num in xrange(1, 1000)])
