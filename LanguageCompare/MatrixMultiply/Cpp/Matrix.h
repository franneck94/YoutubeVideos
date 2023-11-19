#pragma once

#include <algorithm>
#include <exception>
#include <functional>
#include <iostream>
#include <stdexcept>
#include <type_traits>
#include <vector>

template <typename T>
class Matrix
{
public:
    Matrix() = delete;
    Matrix(std::size_t N, const T &value);
    ~Matrix() noexcept = default;

    Matrix(const Matrix &other) = default;
    Matrix &operator=(const Matrix &other) = default;
    Matrix(Matrix &&other) noexcept = default;
    Matrix &operator=(Matrix &&other) noexcept = default;

    Matrix operator*(const Matrix &rhs);
    Matrix &operator*=(const Matrix &rhs);
    void dot(const Matrix &matrix1, const Matrix &matrix2, Matrix &result);

    void print_matrix() const;

    std::size_t N;
    std::vector<T> data;
};

template <typename T>
Matrix<T>::Matrix(std::size_t N, const T &value)
    : N(N), data(N * N, value)
{
}

template <typename T>
Matrix<T> Matrix<T>::operator*(const Matrix<T> &rhs)
{
    Matrix<T> result(N, 0.0);

    dot(*this, rhs, result);

    return result;
}

template <typename T>
Matrix<T> &Matrix<T>::operator*=(const Matrix<T> &rhs)
{
    *this = (*this) * rhs;

    return *this;
}

std::size_t matrixIndex(const std::size_t N, const std::size_t i, const std::size_t j)
{
    return i * N + j;
}

template <typename T>
void Matrix<T>::dot(const Matrix<T> &matrix1, const Matrix<T> &matrix2, Matrix<T> &result)
{
    for (std::size_t i = 0; i != matrix1.N; ++i)
    {
        for (std::size_t k = 0; k != matrix2.N; ++k)
        {
            std::size_t idx_ik = matrixIndex(matrix2.N, i, k);

            for (std::size_t j = 0; j != matrix2.N; ++j)
            {
                std::size_t idx_ij = matrixIndex(matrix2.N, i, j);
                std::size_t idx_kj = matrixIndex(matrix2.N, k, j);

                result.data[idx_ij] += matrix1.data[idx_ik] * matrix2.data[idx_kj];
            }
        }
    }
}

template <typename T>
void Matrix<T>::print_matrix() const
{
    for (std::size_t i = 0; i < N; ++i)
    {
        for (std::size_t j = 0; j < N; ++j)
        {
            std::cout << data[i][j] << " ";
        }

        std::cout << std::endl;
    }

    std::cout << std::endl;
}
