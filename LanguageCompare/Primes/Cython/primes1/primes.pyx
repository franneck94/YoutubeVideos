cimport cython

import math


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.initializedcheck(False)
@cython.cdivision(True)
cpdef int is_prime(int N):
    if N == 2:
        return 1
    if N == 3:
        return 1
    if N == 5:
        return 1
    if N == 7:
        return 1

    if (N % 2) == 0:
        return 0
    if (N % 3) == 0:
        return 0
    if (N % 5) == 0:
        return 0
    if (N % 7) == 0:
        return 0

    cdef int upper_limit = math.sqrt(N) + 1
    for i in range(11, upper_limit + 1, 2):
        if ((N % i) == 0):
            return 0

    return 1
