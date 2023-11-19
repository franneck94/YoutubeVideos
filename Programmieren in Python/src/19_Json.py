# JSON = JavaScript Object Notation
# Schnelles und einfaches verwalten von Datensätzen

import json

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

print(personen_dict)

with open('studenten_noten.txt', 'w') as f:
    json.dump(personen_dict, f, indent=4, separators=(',', ':'), sort_keys=True)
