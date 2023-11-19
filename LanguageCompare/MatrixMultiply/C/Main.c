#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "Matrix.h"
#include "Timer.h"

int main()
{
    uint32_t num_runs = 10000;
    size_t N = 250;

    Matrix *m1 = createMatrix(N, +1.0f);
    Matrix *m2 = createMatrix(N, -1.0f);

    double total_time = 0.0;

    for (uint32_t run_idx = 0; run_idx != num_runs; ++run_idx)
    {
        const clock_t time_start = clock();
        Matrix *m3 = multiplyMatrix(m1, m2);
        const clock_t time_end = clock();
        (void)m3;
        freeMatrix(m3);

        total_time += get_timing_milliseconds(&time_start, &time_end);
    }

    printf("Mean execution time: %.4lf ms", total_time / (double)(num_runs));

    freeMatrix(m1);
    freeMatrix(m2);

    return 0;
}
