# Wie Auf, Keys, Values zugreifen?

tagebuch = {'montag': 'Doofer Tag', 'dienstag': 'War schon besser'}

tagebuch2 = {'montag': ['Schule doof', 'alles doof'],
             'dienstag': ['Schule doof', 'ich bin aber cool']}

# for val in tagebuch:
#     print(val)

for k in tagebuch.keys():
    print(k)

for k, v in tagebuch.items():
    print(k, '  --  ', v)

for v in tagebuch.values():
    print(v)

for k, liste in tagebuch2.items():
    print('key: ', k)
    for val in liste:
        print(val)
