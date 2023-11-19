using System;
using System.Diagnostics;
using System.Collections;

class Matrix
{
    public static void matrixMultiply(
        List<float> matrix1,
        List<float> matrix2,
        List<float> result,
        int N
    )
    {
        {
            for (int i = 0; i != N; i++)
            {
                for (int k = 0; k != N; k++)
                {
                    int idx_ik = N * i + k;

                    for (int j = 0; j != N; j++)
                    {
                        int idx_ij = N * i + j;
                        int idx_kj = N * k + j;
                        result[idx_ij] = result[idx_ij] + matrix1[idx_ik] * matrix2[idx_kj];
                    }
                }
            }
        }
    }

    public static void initMatrix(
            List<float> matrix,
            int N,
            float value)
    {
        for (int i = 0; i < N * N; i++)
        {
            matrix.Add(value);
        }
    }

    static void Main(string[] args)
    {
        int N = 250;
        int num_runs = 1000;
        double total_time = 0.0;

        List<float> matrix1 = new List<float>();
        List<float> matrix2 = new List<float>();

        initMatrix(matrix1, N, +1.0f);
        initMatrix(matrix2, N, -1.0f);

        for (int i = 0; i < num_runs; i++)
        {
            Stopwatch sw = new Stopwatch();
            List<float> matrix3 = new List<float>();
            initMatrix(matrix3, N, +0.0f);
            sw.Start();
            matrixMultiply(matrix1, matrix2, matrix3, N);
            sw.Stop();
            TimeSpan elapsedTime = sw.Elapsed;
            total_time += elapsedTime.TotalMilliseconds;
        }

        double mean_duration = total_time / num_runs;
        var output = string.Format("Mean time: {0:0.##}", mean_duration);
        Console.WriteLine(output);
    }
}
