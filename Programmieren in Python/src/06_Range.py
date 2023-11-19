# Range Anweisungen

# range(start, stop, step)
# range(0, 3, 1) => 0, 1, 2
# range(3)

for i in range(0, 3, 1):
    zahl = int(input('Geben Sie eine Zahl ein!\n'))

    if zahl < 10:
        print('Fall 1')
    elif zahl >= 10 and zahl < 20:
        print('Fall 2')
    else:
        print('Fall 3')

# 10, 12, 14, 16, 18, 20
# 10, 13, 16, 19
for i in range(10, 21, 3):
    print(i)
