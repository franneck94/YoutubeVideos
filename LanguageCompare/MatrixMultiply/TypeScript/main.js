var Matrix = /** @class */ (function () {
    function Matrix(N, data) {
        this.N = N;
        this.data = new Array(N).fill(new Array(N).fill(data));
    }
    Matrix.multiply = function (matrix1, matrix2) {
        var result = new Matrix(matrix1.N, 0.0);
        for (var i = 0; i < matrix1.N; i++) {
            for (var k = 0; k < matrix1.N; k++) {
                for (var j = 0; j < matrix1.N; j++) {
                    result.data[i][j] +=
                        matrix1.data[i][k] * matrix2.data[k][j];
                }
            }
        }
        return result;
    };
    return Matrix;
}());
function main() {
    var num_runs = 100;
    var N = 250;
    var m1 = new Matrix(N, +1.0);
    var m2 = new Matrix(N, -1.0);
    var total_time = 0.0;
    for (var i = 0; i < num_runs; i++) {
        var time_start = performance.now();
        var m3 = Matrix.multiply(m1, m2);
        var time_end = performance.now();
        total_time += time_end - time_start;
    }
    console.log("Mean execution time: " + total_time / num_runs + " ms");
}
main();
