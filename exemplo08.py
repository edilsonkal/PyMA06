from os import system
import numpy as np

from exemplo_matriz04 import matriz_01

system('cls')
matriz_01=[[1,2],[3,4]]
matriz_02=[[5,6],[7,8]]

inversa = np.linalg.inv(matriz_01)
print(inversa)