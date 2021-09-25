#!/usr/bin/python3
import numpy as np

T = np.matrix(
[
    [0.3, 0.3, 0.4],
    [0.2, 0.5, 0.2],
    [0.5, 0.2, 0.4]
]
)

S = np.matrix([[0.1],[0.3],[0.6]])
for i in range(5):
    S = np.matmul(T, S)
    print(S)
    print('')
