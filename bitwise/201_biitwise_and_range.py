#  The bitwise AND of all the numbers in range [m, n] is just the bitwise AND of the two special number

#11000 -> 1 << 4
#10100 -> 1 << 4


def rangeBitwiseAnd(self, m, n):
    i = 0
    while m != n:
        m >>= 1
        n >>= 1
        i += 1
    return n << i