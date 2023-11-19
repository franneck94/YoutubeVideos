# Funktionen, Module

# Aufgabe:
# Schreibe eine Funktion, die die Zahl PI
# annähert.
# Formel:
# x_i = (i - (1/2)) / n
# f(x_i) = 4 / (1 + x_i^2)
# PI = 1/n * Sum_1^n f(x_i)
# (starte bei i=1 gehe bis n)
#
# Zusatzaufgabe: Vergleiche es  mit Numpys PI
# Wie viele Nachkommastellen stimmen mit n=100, 1000, 10000
# überein?

import numpy as np
pi = np.pi
