def is_triplet(number_list):
    if (a < b) and (b < c):
        return ((a * a) + (b * b)) == (c * c)
    return False


for a in xrange(3, 1000 / 3):
    for b in xrange(a+1, (1000 - a) / 2):
        c = 1000 - a - b

        if is_triplet([a, b, c]):
            print a, b, c
            print int(a * b * c)
