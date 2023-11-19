# Benötigtes Wissen: Listen, Ranges

# Aufgabe:
# Lege eine Liste "data" mit zufälligen Werten an.
# Lese dann per Nutzereingabe eine Integer Variable ein.
# Iteriere dann über alle Werte der data Liste.
# Entscheiden beim iterieren der Liste "data", ob der aktuelle
# Wert kleiner als die Nutzereingabe ist => Der Wert kommt in die "smaller"
# Liste oder bei einem größeren Wert in die "bigger" Liste abgespeichert wird.
#
# Zusatzaufgabe: Die Zufallsliste mit List Comp anlegen!

import random # random.randint(LB, UB) erzeugt eine Zufalls Intergerzahl LB <= x <= UB

# Die beiden leeren Listen anlegen
smaller = []
bigger = []
# Zufallsliste anlegen
data = [random.randint(0, 10) for _ in range(10)]
# User Input
user_input = int(input('Gebe eine Ganzezahl ein!\n'))

for val in data:
    if val < user_input:
        smaller.append(val)
    elif val > user_input:
        bigger.append(val)

print(data)
print(smaller)
print(bigger)
