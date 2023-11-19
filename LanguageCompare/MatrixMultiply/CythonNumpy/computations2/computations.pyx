import numpy as np

cimport cython
cimport numpy as np


ctypedef np.float32_t DTYPE_t


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.initializedcheck(False)
cpdef void matrixMultiply(
    np.ndarray[DTYPE_t, ndim=2] matrix1,
    np.ndarray[DTYPE_t, ndim=2] matrix2,
    np.ndarray[DTYPE_t, ndim=2] matrix_result
):
    cdef int i_ = matrix1.shape[0]
    cdef int j_ = matrix1.shape[1]
    cdef int k_ = matrix2.shape[1]

    for i in range(i_):
        for k in range(k_):
            for j in range(j_):
                matrix_result[i, j] += matrix1[i, k] * matrix2[k, j]
