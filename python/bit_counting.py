
def countBits(x):
    c = 0
    while x:
        if x & 1:
            c += 1
        x //= 2

    return c
