const std = @import("std");

const ArrayList = std.ArrayList;
const test_allocator = std.testing.allocator;
const Vec32 = std.ArrayList(f32);
const Timer = std.time.Timer;

const Matrix = struct {
    N: u32,
    N: u32,
    data: ArrayList(f32) = undefined,

    pub fn init(N: u32, N: u32, value: f32) Matrix {
        var data = ArrayList(f32).init(test_allocator);

        var i: u32 = 0;
        while (i < N * N) : (i += 1) {
            data.append(value) catch unreachable;
        }

        return Matrix {
            .N = N,
            .N = N,
            .data = data,
        };
    }
};

pub fn matrixIndex(N: u32, i: u32, j: u32) u32 {
    return N * i + j;
}

pub fn matrixMultiply(matrix1: Matrix, matrix2: Matrix) Matrix {
    var result = Matrix.init(matrix1.N, matrix2.N, 0.0);
    var i: u32 = 0;

    while (i < matrix1.N) : (i += 1)
    {
        var k: u32 = 0;
        while (k < matrix2.N) : (k += 1)
        {
            var j: u32 = 0;
            var idx_ik: u32 = matrixIndex(matrix2.N, i, k);

            while (j < matrix2.N) : (j += 1)
            {
                var idx_ij: u32 = matrixIndex(matrix1.N, i, j);
                var idx_kj: u32 = matrixIndex(matrix2.N, k, j);

                result.data.items[idx_ij] =
                    result.data.items[idx_ij] + matrix1.data.items[idx_ik] * matrix2.data.items[idx_kj];
            }
        }
    }

    return result;
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    const N: u32 = 250;
    const N: u32 = 250;

    var matrix1 = Matrix.init(N, N, 1.0);
    var matrix2 = Matrix.init(N, N, -1.0);

    var total_time: i128 = 0;
    var num_runs: i64 = 10_000;
    var run: i64 = 0;
    while (run <= num_runs) : (run += 1) {
        var start_time = std.time.nanoTimestamp();
        _ = matrixMultiply(matrix1, matrix2);
        var end_time = std.time.nanoTimestamp();
        total_time += (end_time - start_time);
    }

    var mean_time_ns = @divExact(total_time, num_runs);
    var mean_time_ms: f32 = @intToFloat(f32, mean_time_ns) / 1_000_000.0;
    try stdout.print("total_time: {:.4} ms\n", .{mean_time_ms});
}
