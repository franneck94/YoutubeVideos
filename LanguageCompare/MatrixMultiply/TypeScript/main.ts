class Matrix {
    public data: number[][];

    constructor(public N: number, data: number) {
        this.data = new Array(N).fill(new Array(N).fill(data));
    }

    public static multiply(matrix1: Matrix, matrix2: Matrix): Matrix {
        var result = new Matrix(matrix1.N, 0.0);

        for (let i = 0; i < matrix1.N; i++) {
            for (let k = 0; k < matrix1.N; k++) {
                for (let j = 0; j < matrix1.N; j++) {
                    result.data[i][j] +=
                        matrix1.data[i][k] * matrix2.data[k][j];
                }
            }
        }

        return result;
    }
}

function main() {
    const num_runs = 100;
    const N = 250;

    const m1 = new Matrix(N, +1.0);
    const m2 = new Matrix(N, -1.0);

    let total_time = 0.0;

    for (let i = 0; i < num_runs; i++) {
        const time_start = performance.now();
        const m3 = Matrix.multiply(m1, m2);
        const time_end = performance.now();

        total_time += time_end - time_start;
    }

    console.log(`Mean execution time: ${total_time / num_runs} ms`);
}

main();
