# Enumerates, einfaches Indexieren und iterieren von Daten

smaller = [1, 2, 3]
names = ['jan', 'peter', 'horst']

for number, (indx_names, name) in zip(smaller, enumerate(names)):
    print(number, indx_names, name)
