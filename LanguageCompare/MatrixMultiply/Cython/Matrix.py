from __future__ import annotations

import array


class Matrix:
    def __init__(self, N: int, value: float) -> None:
        self.N = N
        self.data = array.array(
            'f', [value for _ in range(N * N)]
        )
