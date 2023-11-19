#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <stdint.h>
#include <math.h>

#include "Timer.h"

bool is_prime(const uint32_t N)
{
    if (N == 2) return true;
    if (N == 3) return true;
    if (N == 5) return true;
    if (N == 7) return true;

    if ((N % 2) == 0) return false;
    if ((N % 3) == 0) return false;
    if ((N % 5) == 0) return false;
    if ((N % 7) == 0) return false;

    uint32_t upper_limit = sqrt(N) + 1;
    for (uint32_t i = 11; i < upper_limit; i += 2)
    {
        if ((N % i) == 0) return false;
    }

    return true;
}

int main()
{
    uint32_t num_runs = 100;
    double total_time = 0.0;

    for (uint32_t run_idx = 0; run_idx != num_runs; ++run_idx)
    {
        uint32_t num_primes = 0;
        const clock_t time_start = clock();

        for (uint32_t i = 200000; i != 400000; ++i)
        {
            bool prime = is_prime(i);
#ifndef NDEBUG
            printf("%u is prime: %d\n", i, prime);
#endif
            if (prime)
            {
                num_primes++;
            }
        }

        const clock_t time_end = clock();
        total_time += get_timing_milliseconds(&time_start, &time_end);
        printf("Num primes %u\n", num_primes);
    }

    printf("Mean execution time: %.4lf ms", total_time / (double)(num_runs));

    return 0;
}
