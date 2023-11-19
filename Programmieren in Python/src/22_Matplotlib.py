# Die Basics für Matplotlib Grafiken

import matplotlib.pyplot as plt

data = [1, 0, 7, 8, 10]

plt.plot(data, c='r')
x1 = 0
x2 = 5
y1 = 3
y2 = 5
plt.plot((x1, x2), (y1, y2), c='y')
plt.scatter(range(len(data)), data, c='b')

plt.xlabel('x werte')
plt.ylabel('y werte')

plt.show()
