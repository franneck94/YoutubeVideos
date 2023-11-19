def p10(inp):
    bits = []
    for i in [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]:
        bits.append(inp[i - 1])
    return bits


def p8(inp):
    bits = []
    for i in [6, 3, 7, 4, 8, 5, 10, 9]:
        bits.append(inp[i - 1])
    return bits


def shift(inp, size=1):
    new = inp[:5]
    old = inp[5:]
    for i in range(size):
        new.insert(5, new.pop(0))
        old.insert(5, old.pop(0))
    return new + old


def keys(K):
    k1 = p8(shift(p10(K)))
    k2 = p8(shift(p10(K), 3))
    return k1, k2
