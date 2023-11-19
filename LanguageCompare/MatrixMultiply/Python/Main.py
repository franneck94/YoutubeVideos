import sys
import time

from Matrix import Matrix


def main() -> int:
    N = 250
    num_runs = 20

    m1 = Matrix(N, +1.0)
    m2 = Matrix(N, -1.0)

    total_time = 0.0
    num_runs = 10

    for _ in range(num_runs):
        time_start = time.time()
        m3 = m1 * m2  # noqa: F841
        time_end = time.time()

        total_time += (time_end - time_start) * 1000.0

    print(f"Mean execution time: {total_time / num_runs} ms")

    return 0


if __name__ == "__main__":
    sys.exit(main())
