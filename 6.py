import numpy as np

a = (np.random.random((5, 5))*10)//1
print("Matrix")
print(a)

print("\nSum")
print(np.sum(a))

print("\nSum of column")
print(np.sum(a, axis=0))

print("\nSum of row")
print(np.sum(a, axis=1))
