import operator


def thirteen_digits(number):
    number = str(number)
    for i in xrange(0, (len(number) - 13)):
        yield number[i:i+13]

with open('1000-digit-number.txt') as f:
    number = f.read().strip()

greatest_product = 0
for digits in thirteen_digits(number):
    greatest_product = max(greatest_product,
                           reduce(operator.mul, [int(d) for d in digits]))

print greatest_product
