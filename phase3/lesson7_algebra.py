def add_vectors(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]


def dot_product(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))


def matrix_multiply_by_scalar(matrix, scalar):
    """Multiply every element in a matrix by a scalar"""
    return [[matrix[i][j] * scalar for j in range(len(matrix[i]))]
            for i in range(len(matrix))]


def matrix_transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    return [[matrix[i][j] for i in range(rows)]
            for j in range(cols)]
v1 = [2, 4, 6]
v2 = [1, 3, 5]

print(add_vectors(v1, v2))
print(dot_product(v1, v2))

matrix = [[1, 2], [3, 4], [5, 6]]

print(matrix_multiply_by_scalar(matrix, 2))
print(matrix_transpose(matrix))



def dot_product(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))


def predict(weights, features):
    return dot_product(weights, features)


weights = [0.4, 0.3, 0.3]

students = [
    [8, 90, 85],
    [3, 60, 45],
    [6, 75, 70]
]

for student in students:
    print(predict(weights, student))