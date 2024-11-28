from os import system
import numpy as np
system('cls')

matriz_01= [[1,2],[3,4]]
matriz_02= [[5,6],[7,8]]
produto = np.dot(matriz_01,matriz_02)
print(produto)