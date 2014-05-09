sum_of_squares = sum([x ** 2 for x in xrange(1, 101)])
square_of_sum = sum(xrange(1, 101)) ** 2

print square_of_sum - sum_of_squares
