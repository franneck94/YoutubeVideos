# While Schleife

zahl = 0.0
ergebnis = 25
weiterspielen = True
zufalls_zahl = 14

while weiterspielen:
    zahl = int(input('Geben Sie eine Zahl ein!\n'))

    if zahl < zufalls_zahl:
        print('Zu niedrig')
    elif zahl == zufalls_zahl:
        print('Gewonnen!')
        break
    else:
        print('Zu Hoch')

    weiterspielen = int(input('Weiterspielen? (0 oder 1)!\n'))
