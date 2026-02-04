import numpy as np

x = np.arange(7, 16)        # [7, 8, 9, ..., 15]
y = np.arange(1, 18, 2)     # [1, 3, 5, ..., 17]

z = np.column_stack((x[::-1], y))

for i, j in z:
    print(' ' * i + '*' * j)

for r in range(3):
    print(' ' * 13 + ' || ')

print(' ' * 12 + '\\ ====== /')
