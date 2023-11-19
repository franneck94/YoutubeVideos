# IF, ELIF, ELSE Abfragen

zahl = 0.0
zahl = int(input('Geben Sie eine Zahl ein!\n'))

if zahl < 10:
    print('Fall 1')
elif zahl >= 10 and zahl < 20:
    print('Fall 2')
else:
    print('Fall 3')
