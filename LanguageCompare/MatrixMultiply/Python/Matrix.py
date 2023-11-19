from __future__ import annotations


class Matrix:
    def __init__(self, N: int, value: float) -> None:
        self.N = N
        self.data = [[value for _ in range(N)] for _ in range(N)]

    def __mul__(self, other: Matrix) -> Matrix:
        result = Matrix(self.N, 0.0)

        for i in range(self.N):
            for k in range(other.N):
                for j in range(other.N):
                    result.data[i][j] += (
                        self.data[i][k]
                        * other.data[k][j]
                    )

        return result
