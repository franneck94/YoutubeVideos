package main

import (
	"fmt"
	"time"
)

type Matrix struct {
	Data []float32
	N    uint
}

func buildMatrix(N uint, value float32) Matrix {
	cap := N * N
	matrix := Matrix{
		Data: make([]float32, cap),
		N:    N,
	}

	for i := range matrix.Data {
		matrix.Data[i] = value
	}
	return matrix
}

func (lhs Matrix) get_value(i, j uint) float32 {
	return lhs.Data[i*lhs.N+j]
}

func (lhs Matrix) set_value(i, j uint, value float32) {
	lhs.Data[i*lhs.N+j] = value
}

func (lhs Matrix) multiply(rhs Matrix) Matrix {
	result := buildMatrix(lhs.N, 0.0)

	for i := uint(0); i < lhs.N; i++ {
		for k := uint(0); k < rhs.N; k++ {
			for j := uint(0); j < rhs.N; j++ {
				result.set_value(i, j, result.get_value(i, j)+lhs.get_value(i, k)*rhs.get_value(k, j))
			}
		}
	}
	return result
}

func main() {
	var numRuns int32 = 100
	var duration time.Duration

	var N uint = 250

	matrix1 := buildMatrix(N, 1.0)
	matrix2 := buildMatrix(N, -1.0)

	for i := int32(0); i < numRuns; i++ {
		start := time.Now()
		_ = matrix1.multiply(matrix2)
		duration += time.Since(start)
	}

	fmt.Println("Mean Time: " + (duration / time.Duration(numRuns)).String())
}
