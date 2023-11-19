import sys
import time

from Matrix import Matrix
from computations2 import matrixMultiply


def main() -> int:
    N = 250
    num_runs = 10_000

    m1 = Matrix(N, +1.0)
    m2 = Matrix(N, -1.0)
    m3 = Matrix(N, 0.0)

    total_time = 0.0
    num_runs = 10

    for _ in range(num_runs):
        time_start = time.time()
        matrixMultiply(
            m1.data,
            m2.data,
            m3.data,
        )
        time_end = time.time()
        total_time += (time_end - time_start) * 1000.0

    print(f"Mean execution time: {total_time / num_runs:.4f} ms")

    return 0


if __name__ == "__main__":
    sys.exit(main())
