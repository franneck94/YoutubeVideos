import itertools
import operator

from key import keys


def ip(inp):
    bits = []
    for i in [2, 6, 3, 1, 4, 8, 5, 7]:
        bits.append(inp[i - 1])
    return bits


def ip_1(inp):
    bits = []
    for i in [4, 1, 3, 5, 7, 2, 8, 6]:
        bits.append(inp[i - 1])
    return bits


def ep(inp):
    bits = []
    for i in [4, 1, 2, 3, 2, 3, 4, 1]:
        bits.append(inp[i - 1])
    return bits


def xor(var1, var2):
    assert(len(var1) == len(var2))
    bits = [operator.xor(var1[i], var2[i]) for i in range(len(var1))]
    return bits


def s(inp, inp_index):
    assert(len(inp) == 4)
    assert(inp_index == 0 or inp_index == 1)

    if [inp[0], inp[3]] == [0, 0]:
        if [inp[1], inp[2]] == [0, 0]:
            s = [0, 1], [0, 0]
        if [inp[1], inp[2]] == [0, 1]:
            s = [0, 0], [0, 1]
        if [inp[1], inp[2]] == [1, 0]:
            s = [1, 1], [1, 0]
        if [inp[1], inp[2]] == [1, 1]:
            s = [1, 0], [1, 1]

    if [inp[0], inp[3]] == [0, 1]:
        if [inp[1], inp[2]] == [0, 0]:
            s = [1, 1], [1, 0]
        if [inp[1], inp[2]] == [0, 1]:
            s = [1, 0], [0, 0]
        if [inp[1], inp[2]] == [1, 0]:
            s = [0, 1], [0, 1]
        if [inp[1], inp[2]] == [1, 1]:
            s = [0, 0], [1, 1]

    if [inp[0], inp[3]] == [1, 0]:
        if [inp[1], inp[2]] == [0, 0]:
            s = [0, 0], [1, 1]
        if [inp[1], inp[2]] == [0, 1]:
            s = [1, 0], [0, 0]
        if [inp[1], inp[2]] == [1, 0]:
            s = [0, 1], [0, 1]
        if [inp[1], inp[2]] == [1, 1]:
            s = [1, 1], [0, 0]

    if [inp[0], inp[3]] == [1, 1]:
        if [inp[1], inp[2]] == [0, 0]:
            s = [1, 1], [1, 0]
        if [inp[1], inp[2]] == [0, 1]:
            s = [0, 1], [0, 1]
        if [inp[1], inp[2]] == [1, 0]:
            s = [1, 1], [0, 0]
        if [inp[1], inp[2]] == [1, 1]:
            s = [1, 0], [1, 1]
    return s[inp_index]


def p4(inp):
    bits = []
    for i in [2, 4, 3, 1]:
        bits.append(inp[i - 1])
    return bits


def sw(inp):
    return inp[4:] + inp[:4]


def fk(inp, k):
    L = inp[:4]
    R = inp[4:]
    sub_result = ep(R)
    sub_result = xor(sub_result, k)
    sub_result = s(sub_result[:4], 0) + s(sub_result[4:], 1)
    sub_result = p4(sub_result)
    sub_result = xor(L, sub_result)
    return sub_result + R


def sdes(M, K, s_inp='cod'):
    if s_inp == 'cod':
        k1, k2 = keys(K)
    elif s_inp == 'dec':
        k2, k1 = keys(K)
    sdes = ip(M)
    sdes = fk(sdes, k1)
    sdes = sw(sdes)
    sdes = fk(sdes, k2)
    sdes = ip_1(sdes)
    return sdes


def cbc_mode_enc(M, K, IV):
    y = []
    for i, m in enumerate(M):
        if i == 0:
            y_i1 = IV
        xor_res = xor(m, y_i1)
        y_i1 = sdes(xor_res, K, 'cod')
        y.append(y_i1)
    return y


def cbc_mode_dec(Y, K, IV):
    x = []
    for i, y in enumerate(Y):
        if i == 0:
            y_i1 = IV
        dk = sdes(y, K, 'dec')
        xi = xor(dk, y_i1)
        x.append(xi)
        y_i1 = y
    return x


def cbc():
    Y = [[0, 1, 0, 0, 0, 0, 1, 1], [0, 1, 1, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0, 0, 1],
         [0, 1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 1, 1, 1]]
    Y_error = [[0, 1, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0, 0, 1],
               [0, 1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 1, 1, 1]]
    K = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
    IV = [1, 0, 0, 0, 1, 0, 1, 1]
    cbc_y = cbc_mode_dec(Y, K, IV)
    cbc_error_y = cbc_mode_dec(Y_error, K, IV)
    for i in range(len(cbc_y)):
        if cbc_y[i] != cbc_error_y[i]:
            print("Error at i = ", i + 1)
            print("Output R: ", cbc_y[i])
            print("Output E: ", cbc_error_y[i])


def k1_to_k(k1):
    return [k1[0], "a2", k1[5], k1[3], "a1", k1[7], k1[1], k1[4], k1[2], k1[6]]


def k2_to_k(k2):
    return [k2[7], k2[3], k2[1], "a2", k2[5], k2[2], "a1", k2[0], k2[6], k2[4]]


def equal(k1, k2):
    for i in range(len(k1)):
        if not(k1[i] == k2[i] or k1[i] in ["a1", "a2"] or k2[i] in ["a1", "a2"]):
            return False
    return True


def k_testing():
    S0_1 = [[0, 1, 0, 0], [0, 0, 0, 1], [1, 1, 1, 0], [1, 0, 0, 1]]
    S1_1 = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 1, 1, 1]]
    R0 = [1, 1, 1, 0, 1, 0, 1, 1]
    K1 = [prod for prod in itertools.product(S0_1, S1_1)]
    K1 = [x + y for (x, y) in K1]

    S0_2 = [[0, 0, 0, 0], [0, 1, 0, 1], [1, 1, 0, 0], [1, 0, 1, 1]]
    S1_2 = [[0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 1, 1, 1]]
    R1 = [0, 1, 0, 1, 0, 1, 0, 1]
    K2 = [prod for prod in itertools.product(S0_2, S1_2)]
    K2 = [x + y for (x, y) in K2]

    K1_K = [k1_to_k(k1) for k1 in K1]
    K2_K = [k2_to_k(k2) for k2 in K2]

    for i in range(len(K1_K)):
        for j in range(len(K2_K)):
            if equal(K1_K[i], K2_K[j]):
                print("Found match!")
                print(K1[i])
                print(K2[j])


def brute_force():
    x = [1, 0, 0, 1, 0, 1, 1, 1]
    y = [1, 0, 1, 1, 1, 0, 0, 0]
    keys = [[int(c) for c in "".join(seq)] for seq in itertools.product("01", repeat=10)]
    K = []
    for key in keys:
        y_test = sdes(x, key, 'cod')
        if y == y_test:
            print("Found key: ", key)
            K = key
            break
    print("Finished!")


if __name__ == '__main__':
    # cbc()
    brute_force()
    # k_testing()
