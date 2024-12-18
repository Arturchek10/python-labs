# 6.Написать функцию, которая принимает матрицу и возвращает её определитель.

import numpy as np

def calculate_determinant(matrix):

  #список списков преобраз в numpy массив
  np_matrix = np.array(matrix)
  #  матрица квадратная?
  if np_matrix.shape[0] != np_matrix.shape[1]:
      raise ValueError("Матрица должна быть квадратной.")
  # вычисляем определитель
  determinant = np.linalg.det(np_matrix)
  return determinant

# примеры использования
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

det = calculate_determinant(matrix)
print(f"Определитель матрицы: {det}")

matrix2 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]

det = calculate_determinant(matrix2)
print(f"Определитель матрицы: {det}")