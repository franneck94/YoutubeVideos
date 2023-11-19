import java.lang.System;
import java.lang.Math;

class Primes {
    public static Boolean is_prime(int N) {
        if (N == 2)
            return true;
        if (N == 3)
            return true;
        if (N == 5)
            return true;
        if (N == 7)
            return true;

        if ((N % 2) == 0)
            return false;
        if ((N % 3) == 0)
            return false;
        if ((N % 5) == 0)
            return false;
        if ((N % 7) == 0)
            return false;

        int upper_limit = (int) Math.sqrt(N) + 1;
        for (int i = 11; i < upper_limit; i += 2) {
            if ((N % i) == 0)
                return false;
        }

        return true;
    }

    public static void main(String[] args) {
        int num_runs = 100;
        double total_time = 0.0;

        for (int run_idx = 0; run_idx != num_runs; ++run_idx) {
            int num_primes = 0;
            long startTime = System.currentTimeMillis();

            for (int i = 200000; i != 400000; ++i) {
                Boolean prime = is_prime(i);
                if (prime) {
                    num_primes++;
                }
            }

            long stopTime = System.currentTimeMillis();
            long elapsedTime = stopTime - startTime;
            total_time += elapsedTime;
            System.out.println("Num primes: " + Integer.toString(num_primes));
        }

        System.out.println("Mean time: " + Double.toString(total_time / (num_runs)));
    }
}
