import numpy as np

# Vamos criar uma array (vetor)

arr = np.array([1, 2, 3, 4, 5])

print(f'Array {arr}')

# Vamos multiplicar nossa array
print(arr * 2)

# Vamos somar nossa array
arr2= np.array([10, 20, 30, 40, 50])
print (arr + arr2)

# Vamos criar uma matriz 2d
matriz = np.array([[1,2,3] , [4,5,6]])
print(matriz)

# Transposta da matriz
print(matriz.T)

# Gerando uma matriz com valores aleatorios
print(np.random.rand(3,3))