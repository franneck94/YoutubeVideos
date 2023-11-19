using System.Diagnostics;

class Primes
{
    public static bool is_prime(int N)
    {
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

        int upper_limit = (int)Math.Sqrt(N) + 1;
        for (int i = 11; i < upper_limit; i += 2)
        {
            if ((N % i) == 0)
                return false;
        }

        return true;
    }

    static void Main(string[] args)
    {
        int num_runs = 100;
        double total_time = 0.0;

        for (int run_idx = 0; run_idx != num_runs; ++run_idx)
        {
            int num_primes = 0;
            Stopwatch sw = new Stopwatch();
            sw.Start();
            for (int i = 200000; i != 400000; ++i)
            {
                bool prime = is_prime(i);
                if (prime)
                {
                    num_primes++;
                }
            }
            sw.Stop();
            TimeSpan elapsedTime = sw.Elapsed;
            total_time += elapsedTime.TotalMilliseconds;
            var output_primes = string.Format("Num primes: {0:0.##}", num_primes);
            Console.WriteLine(output_primes);
        }

        double mean_duration = total_time / num_runs;
        var output_time = string.Format("Mean time: {0:0.##}", mean_duration);
        Console.WriteLine(output_time);
    }
}
