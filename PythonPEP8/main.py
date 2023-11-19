from __future__ import division

import random

import numpy as np

from module import M


my_value = random.random()
b = my_value * my_value

c = my_value / M


def f(a: float) -> float:
    return int(np.random.randint(0, 5)) * a

my_name: str = "Jan"
my_result = f(my_name)
