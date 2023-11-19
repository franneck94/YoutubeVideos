const std = @import("std");
const print = @import("std").debug.print;

const Timer = std.time.Timer;

pub fn is_prime(N: u32) bool
{
    if (N == 2) return true;
    if (N == 3) return true;
    if (N == 5) return true;
    if (N == 7) return true;

    if ((N % 2) == 0) return false;
    if ((N % 3) == 0) return false;
    if ((N % 5) == 0) return false;
    if ((N % 7) == 0) return false;

    var upper_limit: u32 = @floatToInt(u32, @sqrt(@intToFloat(f32, N))) + 1;
    var i: u32 = 11;
    while (i <= upper_limit) : (i += 2) {
        if (@mod(N, i) == 0) return false;
    }

    return true;
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    var total_time: i128 = 0;
    var num_runs: i64 = 100;

    var run: i64 = 0;

    while (run <= num_runs) : (run += 1) {
        var number: u32 = 200_000;
        var num_primes: u32 = 0;
        var start_time = std.time.nanoTimestamp();

        while (number <= 400_000) : (number += 1) {
            var prime: bool = is_prime(number);

            if (prime)
            {
                num_primes += 1;
            }
        }

        var end_time = std.time.nanoTimestamp();
        total_time += (end_time - start_time);
        try stdout.print("num primes: {}\n", .{num_primes});
    }

    var mean_time_ns = @divFloor(total_time, num_runs);
    var mean_time_ms: f32 = @intToFloat(f32, mean_time_ns) / 1_000_000.0;
    try stdout.print("total_time: {:.4} ms\n", .{mean_time_ms});
}
