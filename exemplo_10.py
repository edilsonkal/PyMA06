
import numpy as np



a = np.array([[2,3],[1,4]])
b =np.array([5,6])

x = np.linalg.solve(a,b)
print(x)