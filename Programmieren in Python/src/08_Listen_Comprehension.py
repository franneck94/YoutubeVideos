# Das richtige anlegen von Listen

vector = [0 for _ in range(10)]
print(vector)

vector = [i for i in range(10)]
print(vector)

matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)
