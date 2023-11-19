import java.lang.System;
import java.util.ArrayList;

class Matrix {
    public static void matrixMultiply(
            ArrayList<Float> matrix1,
            ArrayList<Float> matrix2,
            ArrayList<Float> result,
            int N) {
        {
            for (int i = 0; i != N; i++) {
                for (int k = 0; k != N; k++) {
                    int idx_ik = N * i + k;
                    for (int j = 0; j != N; j++) {
                        int idx_ij = N * i + j;
                        int idx_kj = N * k + j;
                        Float temp = result.get(idx_ij) + matrix1.get(idx_ik) * matrix2.get(idx_kj);
                        result.set(idx_ij, temp);
                    }
                }
            }
        }
    }

    public static void initMatrix(
            ArrayList<Float> matrix,
            int N,
            float value) {
        for (int i = 0; i < N * N; i++) {
            matrix.add(i, value);
        }
    }

    public static void main(String[] args) {
        int N = 250;
        int num_runs = 1000;
        double total_time = 0.0;

        ArrayList<Float> matrix1 = new ArrayList<Float>();
        ArrayList<Float> matrix2 = new ArrayList<Float>();

        initMatrix(matrix1, N, +1.0f);
        initMatrix(matrix2, N, -1.0f);

        for (int i = 0; i < num_runs; i++) {
            ArrayList<Float> matrix3 = new ArrayList<Float>();
            initMatrix(matrix3, N, +0.0f);
            long startTime = System.currentTimeMillis();
            matrixMultiply(matrix1, matrix2, matrix3, N);
            long stopTime = System.currentTimeMillis();
            long elapsedTime = stopTime - startTime;
            total_time += elapsedTime;
        }

        System.out.println("Mean time: " + Double.toString(total_time / (num_runs)));
    }
}
