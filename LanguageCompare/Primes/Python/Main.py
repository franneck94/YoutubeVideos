import sys
import time
import math


def is_prime(N: int):
    if N == 2:
        return 1
    if N == 3:
        return 1
    if N == 5:
        return 1
    if N == 7:
        return 1

    if (N % 2) == 0:
        return 0
    if (N % 3) == 0:
        return 0
    if (N % 5) == 0:
        return 0
    if (N % 7) == 0:
        return 0

    upper_limit = int(math.sqrt(N)) + 1
    for i in range(11, upper_limit + 1, 2):
        if ((N % i) == 0):
            return 0

    return 1


def main() -> int:
    num_runs = 10
    total_time = 0.0

    for _ in range(num_runs):
        time_start = time.time()
        num_primes = 0

        for i in range(200000, 400000):
            prime = is_prime(i)
            if prime:
                num_primes += 1
        time_end = time.time()
        total_time += (time_end - time_start) * 1000.0
        print(f"Num primes: {num_primes}")

    print(f"Mean execution time: {total_time / num_runs} ms")

    return 0


if __name__ == "__main__":
    sys.exit(main())
