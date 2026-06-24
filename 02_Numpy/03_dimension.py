# VECTOR : 1 Dimensional
# MATRIX : 2 Dimensional
# TENSOR : 3 Dimensional

import numpy as np
vector = np.array([1,2,3])
print("1 dimensional : \n",vector)

matrix = np.array([[1,2,3],
                   [4,5,6]])
print("2 dimensional : \n",matrix)

tensor = np.array([[[1,2,3],[4,5,6]],
    [[6,7,8],[9,10,11]]
])
print("3 dimensional : \n",tensor)