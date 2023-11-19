# Funktionen, Module

# Aufgabe:
# Schreibe eine Funktion, die die Zahl PI
# annähert.
# Formel:
# x_i = (i - (1/2)) / n
# f(x_i) = 4 / (1 + x_i^2)
# PI = 1/n Sum_1^n f(x_i)
#
# Zusatzaufgabe: Vergleiche es  mit Numpys PI
# Wie viele Nachkommastellen stimmen mit n=100, 1000, 10000
# überein?

import numpy as np


def xi(i, n):
    x = (i - (1.0 / 2.0)) / n
    return x


def fi(xi, n):
    f = 4.0 / (1.0 + xi**2.0)
    return f


def calc_pi():
    n = 1000000
    pi = 0.0
    for i in range(1, n):
        pi += fi(xi(i, n), n)
    pi /= n

    print('Eignes PI: ', pi)
    print('Numpys PI: ', np.pi)


calc_pi()
