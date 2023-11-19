# Erstellen mit Dict Comprehension

studenten = ['jan', 'horst', 'peter']
noten = [1, 1, 3]

stud_dict = {'jan': 1, 'horst': 1, 'peter': 3}
print(stud_dict)

stud_dict2 = {key: val for key, val in zip(studenten, noten)}
print(stud_dict2)
