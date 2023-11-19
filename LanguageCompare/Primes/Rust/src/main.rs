use std::time::Instant;

fn is_prime(N: u32) -> bool {
    match N {
        1 => false,
        2 | 3 | 5 | 7 => true,
        _ if N % 2 == 0 => false,
        _ if N % 3 == 0 => false,
        _ if N % 5 == 0 => false,
        _ if N % 7 == 0 => false,
        _ => {
            let upper_limit = ((N as f32).sqrt() as u32) + 1;
            for i in (11..upper_limit).step_by(2) {
                if N % i == 0 {
                    return false;
                }
            }
            true
        }
    }
}

fn main() {
    let num_runs: i32 = 100;
    let mut total_time: u128 = 0;

    for _ in 0..num_runs {
        let mut num_primes: u32 = 0;
        let start = Instant::now();
        for i in 200000..400000 {
            let prime = is_prime(i);

            if prime {
                num_primes += 1;
            }
        }
        total_time += start.elapsed().as_micros();
        println!("num_primes: {:}", num_primes);
    }

    println!(
        "Mean Time: {:.4} ms",
        ((total_time as f32) / 1000.0) / (num_runs as f32)
    );
}
