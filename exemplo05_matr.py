from os import system
import numpy as np
system('cls')

matriz_2x2 = [[1,2],[3,4]]
determinante = np.linalg.det(matriz_2x2)
print(determinante)