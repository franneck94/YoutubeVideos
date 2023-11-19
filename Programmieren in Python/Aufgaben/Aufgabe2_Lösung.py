# Benötigtes Wissen: Rund um Dictionarys

# Aufgabe:
# Anlegen eines Dictionarys, was für mehrere Personen
# Ihre Vertiefungsgebiete und Noten in einem gemeinsamen
# Dictionary abspeichert. Danach wird dann über das Dict
# iteriert und die einzelnen Werte jeder Person ausgegeben.
#
# Zusatzaufgabe:
# Gebe die Personen aus, die die gleichen Interessen haben!

personen = ['jan', 'peter', 'horst']
präferenz = {'jan': ['AI', 'ITS', 'Mathe'],
             'peter': ['ITS', 'ET', 'Physik'],
             'horst': ['Physik', 'Mathe', 'Chemie']}
noten = {'jan': ['1', '1', '2'],
         'peter': ['3', '2', '2'],
         'horst': ['3', '2', '1']}

personen_dict = {pers: [(fach, note) for fach, note in
                        zip(präferenz[pers], noten[pers])]
                 for pers in personen}

for person, daten in personen_dict.items():
    print('Student: ', person)
    for fach in daten:
        print('Fach: ', fach[0], ' Note: ', fach[1])
