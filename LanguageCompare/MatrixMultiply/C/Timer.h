#ifndef TIMER_H
#define TIMER_H

#include <time.h>

double get_timing_milliseconds(const clock_t *time_start, const clock_t *time_end);

double get_timing_microseconds(const clock_t *time_start, const clock_t *time_end);

double get_timing_nanoseconds(const clock_t *time_start, const clock_t *time_end);

#endif
