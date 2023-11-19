import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'


import sys
import time

import numpy as np


def main() -> int:
    N = 250
    num_runs = 10_000
    total_time = 0.0

    m1 = np.full(shape=(N, N), fill_value=+1.0)
    m2 = np.full(shape=(N, N), fill_value=-1.0)

    for _ in range(num_runs):
        time_start = time.time()
        m3 = np.matmul(m1, m2)  # noqa: F841
        time_end = time.time()

        total_time += (time_end - time_start) * 1000.0

    print(f"Mean execution time: {round(total_time / num_runs, 4)} ms")

    return 0


if __name__ == "__main__":
    sys.exit(main())
