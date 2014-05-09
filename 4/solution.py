max_palindrome = 0

for n in xrange(100, 1000):
    for m in xrange(100, 1000):
        s = str(n*m)
        if s == s[::-1]:
            max_palindrome = max([n*m, max_palindrome])

print max_palindrome
