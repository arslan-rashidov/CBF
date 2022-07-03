import numpy as np

matrix = []

with open('InputWebs', 'r') as f:
    for line in f:
        line = line.replace('\n', '').split(' ')
        for i in range(len(line)):
            line[i] = int(line[i])
        matrix.append(line)

matrix = np.array(matrix)
transpose_matrix = matrix.transpose()

h = np.array([1] * len(matrix))

for i in range(4):
    transpose_matrix_dot_h = transpose_matrix.dot(h)
    max_number = max(transpose_matrix_dot_h)
    a = transpose_matrix_dot_h/max_number
    matrix_dot_a = matrix.dot(a)
    max_number = max(matrix_dot_a)
    h = matrix_dot_a/max_number

print(h)
print(a)