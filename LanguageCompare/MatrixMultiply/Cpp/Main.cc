#include <iostream>
#include <iomanip>
#include <cstdint>

#include "Matrix.h"
#include "Timer.h"

int main()
{
    std::uint32_t num_runs = 10'000;
    std::size_t N = 250;

    Matrix<float> m1(N, +1.0);
    Matrix<float> m2(N, -1.0);

    double total_time = 0.0;

    for (std::uint32_t i = 0; i < num_runs; ++i)
    {
        cpptiming::Timer t;
        Matrix<float> m3 = m1 * m2;
        total_time += t.elapsed_time<cpptiming::microsecs, double>();
#ifndef NDEBUG
        m3.print_matrix();
#endif
    }

    std::cout << "Mean time: " << (total_time / 1000.0) / num_runs << " ms" << std::endl;

    return 0;
}
