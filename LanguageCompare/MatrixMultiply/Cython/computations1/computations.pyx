cimport cython


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.initializedcheck(False)
cpdef void matrixMultiply(
    float[:] matrix1,
    float[:] matrix2,
    float[:] matrix_result,
    int N
):
    cdef int idx_ij = 0
    cdef int idx_ik = 0
    cdef int idx_kj = 0

    for i in range(N):
        for k in range(N):
            idx_ik = N * i + k
            for j in range(N):
                idx_ij = N * i + j
                idx_kj = N * k + j
                matrix_result[idx_ij] += (
                    matrix1[idx_ik] * matrix2[idx_kj]
                )
