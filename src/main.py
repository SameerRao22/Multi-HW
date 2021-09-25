#!/usr/bin/python3
import matrix as m
import calc3codes as c
import numpy as np


M = [
  [1,2],
  [3,1],
]

M2 = [
    [5,0],
    [0,4],
]

#V = [[1],[-2],[1]]
#V = [
#        [0, 1, 1, 0, 0],
#        [0, 0, 1, 1, 0],
#        [0, 0, 0, 0, 0]
#    ]

#m.pPrint(c.mult(M, M2)) #m.pPrint(c.mult(M2, M))

print(m.det(M))
M = np.array(M)
print(np.linalg.inv(M.T))

"""
Transformations

[Sx  0   Tx]
[0   Sy  Ty]
[0   0   1 ]

T = Transform
S = Scale

Reflect about y axis
[-1  0  0]
[ 0  1  0]
[ 0  0  1]

Reflect x axis
[1   0  0]
[0  -1  0]
[0   0  1]
"""
