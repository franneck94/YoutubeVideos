# Sortieren von Datensätzen in Python

import random

data = [random.randint(0, 100) for _ in range(10)]
print(data)

# sorted: neue Liste returned sorted()
# sort: in-place sortierung .sort()

data.sort(reverse=True)
print(data)

data = [random.randint(0, 100) for _ in range(10)]
print(data)

data2 = sorted(data)
print(data2)

name = "jan"
name_sorted = sorted(name)
print(name_sorted)

name = "jan"
name.sort()
print(name)
