import sys
import time

from primes1 import is_prime


def main() -> int:
    num_runs = 100
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
