#include <float.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "Matrix.h"

/**********************/
/*   MAIN FUNCTIONS   */
/**********************/

Matrix *createMatrix(const size_t N, const float value)
{
    Matrix *matrix = (Matrix *)malloc(sizeof(Matrix));

    if (matrix == NULL)
    {
        return NULL;
    }

    float *data = (float *)malloc(N * N * sizeof(float));

    if (data == NULL)
    {
        free(matrix);
        return NULL;
    }

    for (size_t i = 0; i != N * N; ++i)
    {
        data[i] = value;
    }

    matrix->data = data;
    matrix->N = N;

    return matrix;
}

Matrix *freeMatrix(Matrix *matrix)
{
    if (matrix == NULL)
    {
        return NULL;
    }

    if (matrix->data != NULL)
    {
        free(matrix->data);
        matrix->data = NULL;
    }

    free(matrix);
    return NULL;
}

/**********************/
/*  HELPER FUNCTIONS  */
/**********************/

size_t matrixIndex(const size_t N, const size_t i, const size_t j)
{
    return i * N + j;
}

bool matrixMultiplyPossible(const Matrix *const matrix1, const Matrix *const matrix2)
{
    return (matrix1->N == matrix2->N);
}

/**********************/
/*  I/O FUNCTIONS     */
/**********************/

void printMatrix(const Matrix *const matrix)
{
    printf("[");

    for (size_t i = 0; i != matrix->N; ++i)
    {
        if (i == 0)
        {
            printf("[");
        }
        else
        {
            printf(" [");
        }

        for (size_t j = 0; j != matrix->N - 1; ++j)
        {
            const size_t idx = matrixIndex(matrix->N, i, j);

            printf("%f, ", matrix->data[idx]);
        }

        const size_t idx = matrixIndex(matrix->N, i, matrix->N - 1);

        if (i != (matrix->N - 1))
        {
            printf("%f]\n", matrix->data[idx]);
        }
        else
        {
            printf("%f", matrix->data[idx]);
        }
    }

    printf("]]\n\n");
}

/**********************/
/*  MATH. FUNCTIONS   */
/**********************/

Matrix *multiplyMatrix(const Matrix *const matrix1, const Matrix *const matrix2)
{
    Matrix *result = createMatrix(matrix1->N, 0.0f);

    for (size_t i = 0; i != matrix1->N; ++i)
    {
        for (size_t k = 0; k != matrix2->N; ++k)
        {
            size_t idx_ik = matrixIndex(matrix2->N, i, k);

            for (size_t j = 0; j != matrix2->N; ++j)
            {
                size_t idx_ij = matrixIndex(matrix2->N, i, j);
                size_t idx_kj = matrixIndex(matrix2->N, k, j);

                result->data[idx_ij] += matrix1->data[idx_ik] * matrix2->data[idx_kj];
            }
        }
    }

    return result;
}
