def even_fibbonacci():
    last = (0, 1,)

    while last[-1] < 4000000:
        new = sum(last)
        last = (last[1], new,)

        if (new % 2) == 0:
            yield new

print sum(even_fibbonacci())
