# For-Schleife (einfaches iterieren)

# 0, 1, 2
for i in range(3):
    zahl = int(input('Geben Sie eine Zahl ein!\n'))

    if zahl < 10:
        print('Fall 1')
    elif zahl >= 10 and zahl < 20:
        print('Fall 2')
    else:
        print('Fall 3')

einnkaufs_liste = ['apfel', 'birne', 'gemüse']

for item in einnkaufs_liste:
    print(item)
