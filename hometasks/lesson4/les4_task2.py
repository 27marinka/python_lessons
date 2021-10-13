"""
Дано 2 Матрицы
Необходимо получить произведение данных матриц
"""

matrix1 = [
    [3, 5, 6, 3],
    [4, 4, 1, 5]
    ]

matrix2 = [
    [1, 11],
    [2, 22],
    [3, 33],
    [4, 44]
]

result = []

rows_matrix1 = len(matrix1)
cols_matrix1 = len(matrix1[0])
rows_matrix2 = len(matrix2)
cols_matrix2 = len(matrix2[0])

if cols_matrix1 == rows_matrix2:
    # Create the result matrix
    result = [[0 for row in range(cols_matrix2)] for col in range(rows_matrix1)]
    
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
else:
    print("Cannot multiply the two matrix. ")


print(result)


