import numpy as np

a = np.zeros((5,5), dtype=int)
np.fill_diagonal(a, [1, 2, 3, 4, 5])
print(a)
