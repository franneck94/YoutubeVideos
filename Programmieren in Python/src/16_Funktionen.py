# Eigene Funktionen erstellen

def func(a=2, b=6, c=None):
    print('A: ', a)
    print('B: ', b)
    print('C: ', c)
    val = a * b

    return val, a, b


wert, a, b = func(3, 12)
print(wert, a, b)
