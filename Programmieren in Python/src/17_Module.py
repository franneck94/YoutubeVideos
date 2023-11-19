# Module laden und eigene erstellen
import numpy
import numpy as np
from Eignes_Modul import func

print(numpy.mean([1, 2]))
print(np.mean([1, 2]))

from numpy import mean, median
print(mean([1, 2]))

val, a, b = func()
print(val)
