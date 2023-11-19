# Benötigtes Wissen: Numpy und Matplotlib

# Aufgabe:
#
# Lege einen Zufälligen Datensatz an und caste dies zu einem Numpy Array.
# Stelle diese Daten in Matplotlib als Scatterplot dar (Farbe=Blau).
# Beschrifte Dabei die Achsen nach Wahl und zeichne die Linie
# des Mittelwertes der Daten in Rot ein.
#
# Zusatzaufgabe: Gebe ebenfalls den Median aus Gelbe Linie im Plot aus.

import random
import numpy as np
import matplotlib.pyplot as plt

data = [random.randint(val, 2 * val) for val in range(30)]
mean = np.mean(data, dtype=np.float64)
median = np.median(data)

plt.scatter(range(30), data, color='b')
plt.plot((0, 30), (mean, mean), color='r')
plt.plot((0, 30), (median, median), color='y')

plt.xlabel('x')
plt.ylabel('y')

plt.show()
