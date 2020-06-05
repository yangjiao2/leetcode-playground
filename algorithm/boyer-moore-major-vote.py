# For any alignment of P with T the Boyer-Moore algorithm checks for an
# occurrence of P by scanning characters from
# right to left
# rather than from left to right as in the naive algorithm.
#
# skip amount = pattern length - char positioon - 1


def BoyerMooreHorspool(pattern, text):
    m = len(pattern)
    n = len(text)
    if m > n: return -1
    skip = []
    for k in range(256):
        skip.append(m)
    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1: return i + 1
        k += skip[ord(text[k])]
    return -1