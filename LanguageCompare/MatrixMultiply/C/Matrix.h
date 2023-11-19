#ifndef MATRIX_H
#define MATRIX_H

#include <stdbool.h>
#include <stdint.h>

/**********************/
/* DEFINES AND TYPES  */
/**********************/

typedef enum
{
    AXIS_0,
    AXIS_1,
} Axis;

typedef struct
{
    float *data;
    size_t N;
} Matrix;

/**********************/
/*   MAIN FUNCTIONS   */
/**********************/

Matrix *createMatrix(const size_t N, const float value);

Matrix *freeMatrix(Matrix *matrix);

/**********************/
/*  HELPER FUNCTIONS  */
/**********************/

size_t matrixIndex(const size_t N, const size_t i, const size_t j);

bool matrixMultiplyPossible(const Matrix *matrix1, const Matrix *matrix2);

/**********************/
/*  I/O FUNCTIONS     */
/**********************/

void printMatrix(const Matrix *matrix);

/**********************/
/*  MATH. FUNCTIONS   */
/**********************/

Matrix *multiplyMatrix(const Matrix *matrix1, const Matrix *matrix2);

#endif // MATRIX_H
