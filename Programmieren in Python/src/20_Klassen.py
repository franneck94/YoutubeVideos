# Erstellen von eigenen Klassen

class Vector3d:
    x = 0
    y = 0
    z = 0

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def printCoordinates(self):
        print('X: ', self.x)
        print('Y: ', self.y)
        print('Z: ', self.z)


null_vector = Vector3d(0, 0, 0)
null_vector.printCoordinates()

v1 = Vector3d(1, 2, 1)
v1.printCoordinates()
