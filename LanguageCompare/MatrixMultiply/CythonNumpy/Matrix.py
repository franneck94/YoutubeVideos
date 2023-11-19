from __future__ import annotations

import numpy as np


class Matrix:
    def __init__(self, N: int, value: float) -> None:
        self.N = N
        self.data = np.full(shape=(self.N, self.N),
                            fill_value=value, dtype=np.float32)
