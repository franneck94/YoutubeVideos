# ZIP, praktisches Zusammenführen von Daten

smaller = [1, 2, 3]
name = ['jan', 'peter', 'horst']

for val1, val2 in zip(smaller, name):
    print(val1, val2)

neue_liste = list(zip(smaller, name))
print(neue_liste)

for val in neue_liste:
    print(val[0], val[1])
