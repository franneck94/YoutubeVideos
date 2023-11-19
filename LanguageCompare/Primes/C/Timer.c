#include "Timer.h"

double get_timing_milliseconds(const clock_t *time_start, const clock_t *time_end)
{
    clock_t total_time = *time_end - *time_start;
    double seconds = ((double)total_time) / CLOCKS_PER_SEC;

    return 1000.0 * seconds;
}

double get_timing_microseconds(const clock_t *time_start, const clock_t *time_end)
{
    clock_t total_time = *time_end - *time_start;
    double seconds = ((double)total_time) / CLOCKS_PER_SEC;

    return 1000.0 * 1000.0 * seconds;
}

double get_timing_nanoseconds(const clock_t *time_start, const clock_t *time_end)
{
    clock_t total_time = *time_end - *time_start;
    double seconds = ((double)total_time) / CLOCKS_PER_SEC;

    return 1000.0 * 1000.0 * 1000.0 * seconds;
}
