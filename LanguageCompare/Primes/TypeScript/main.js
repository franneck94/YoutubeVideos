function is_prime(N) {
    if (N == 2) return true;
    if (N == 3) return true;
    if (N == 5) return true;
    if (N == 7) return true;
    if (N % 2 == 0) return false;
    if (N % 3 == 0) return false;
    if (N % 5 == 0) return false;
    if (N % 7 == 0) return false;
    var upper_limit = Math.sqrt(N) + 1;
    for (var i = 11; i < upper_limit; i += 2) {
        if (N % i == 0) return false;
    }
    return true;
}
function main() {
    var num_runs = 100;
    var total_time = 0.0;
    for (var run_idx = 0; run_idx != num_runs; ++run_idx) {
        var num_primes = 0;
        var time_start = performance.now();
        for (var i = 200000; i != 400000; ++i) {
            var prime = is_prime(i);
            if (prime) {
                num_primes++;
            }
        }
        var time_end = performance.now();
        total_time += time_end - time_start;
        console.log('Num primes: ' + num_primes);
    }
    console.log('Mean execution time: ' + total_time / num_runs + ' ms');
}
main();
