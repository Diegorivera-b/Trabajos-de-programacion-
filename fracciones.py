A = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

print("Matriz A:", A)
print(type(A))

# Recordar el dato por fila y columna
print("Elemento en la fila 2, columna 3:", A[1][2])  # Accede al elemento en la fila 2, columna 3
print("Elemento en la fila 1, columna 1:", A[0][0])  # Accede al elemento en la fila 1, columna 1

# Recordar la matriz con anidados
for fila in A:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Nueva línea después de cada fila

# Obtener cantidad de filas y columnas
filas = len(A)
columnas = len(A[0])

print("Número de filas:", filas)
print("Número de columnas:", (columnas),(filas))  # Asumiendo que todas las filas tienen la misma cantidad de columnas
#Numpy
import numpy as np
B = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print (type(B))
C = np.array(
    [2, 4, 6]
    [8, 10, 12]
    [14, 16, 18]
)