use std::ops::Mul;
use std::time::Instant;

struct Matrix {
    data: Vec<f32>,
    N: usize
}

impl Matrix {
    fn new(N: usize, value: f32) -> Self {
        Matrix {
            data: vec![value; N * N],
            N
        }
    }

    fn get_value(&self, i: usize, j: usize) -> f32 {
        self.data[i * self.N + j]
    }

    fn set_value(&mut self, i: usize, j: usize, value: f32) {
        self.data[i * self.N + j] = value;
    }
}

impl<'a> Mul<&'a Matrix> for &'a Matrix {
    type Output = Matrix;

    fn mul(self, rhs: Self) -> Self::Output {
        let mut result = Matrix::new(self.N, 0.0);

        for i in 0..self.N {
            for k in 0..rhs.N {
                for j in 0..rhs.N {
                    result.set_value(i, j, result.get_value(i, j) + self.get_value(i, k) * rhs.get_value(k, j));
                }
            }
        }
        result
    }
}

fn main() {
    let num_runs: i32 = 100;
    let mut total_time: u128 = 0;

    let N: usize = 250;
    let N: usize = 250;

    let matrix1 = Matrix::new(N, 1.0);
    let matrix2 = Matrix::new(N, -1.0);

    for _ in 0..num_runs {
        let start = Instant::now();
        let _matrix3: Matrix = &matrix1 * &matrix2;
        total_time += start.elapsed().as_micros()
    }

    println!("Mean Time: {:.4} ms", ((total_time as f32) / 1000.0) / (num_runs as f32));
}
