import os
N = 1
os.environ["OMP_NUM_THREADS"] = f"{N}"
os.environ['TF_NUM_INTEROP_THREADS'] = f"{N}"
os.environ['TF_NUM_INTRAOP_THREADS'] = f"{N}"


import sys
import time

import tensorflow as tf


def main() -> int:
    N = 250
    num_runs = 10_000
    total_time = 0.0

    m1 = tf.fill(dims=[N, N], value=+1.0)
    m2 = tf.fill(dims=[N, N], value=-1.0)
    _ = tf.linalg.matmul(m1, m2)  # dummy call to init tf env

    for _ in range(num_runs):
        time_start = time.time()
        m3 = tf.linalg.matmul(m1, m2)  # noqa: F841
        time_end = time.time()

        total_time += (time_end - time_start) * 1000.0

    print(f"Mean execution time: {round(total_time / num_runs, 4)} ms")

    return 0


if __name__ == "__main__":
    sys.exit(main())
