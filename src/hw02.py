# Sameer Rao
import copy
#scales a matrix M by a factor S
def scale(S, M):
    A = []
    for j in range(len(M)):
        temp = []
        for k in range(len(M[0])):
            temp.append(M[j][k]*S)
        A.append(temp)
    return A

#adds matrix M1 and M2
def add(M1, M2):
    size1 = (len(M1), len(M1[0]))
    size2 = (len(M2), len(M2[0]))
    if size1 != size2:
        return "wrong size"
    S = []
    for j in range(len(M1)):
        temp = []
        for k in range(len(M1[0])):
            temp.append(M1[j][k] + M2[j][k])
        S.append(temp)
    return S

#transposes a matrix M
def transpose(M):
    T = []
    for j in range(len(M[0])):
        temp = []
        for k in range(len(M)):
            temp.append(M[k][j])
        T.append(temp)
    return T

#computes the dot product of 2 vectors
def dotProduct(V1, V2):
    S = 0
    for i in range(len(V1)):
        S += V1[i]*V2[i]
    return S

#multiplies two matrices by first transposing the second matrix and
#dotting each corresponding row
def multiply(M1, M2):
    if len(M1[0])!= len(M2):
        return "wrong size"
    P = []
    T2 = transpose(M2)
    for j in M1:
        r = []
        for k in T2:
            r.append(dotProduct(j,k))
        P.append(r)
    return P

def det(M):
    size = (len(M), len(M[0]))
    if size[0] != size[1]:
        return "Not a Square"

    if size[0] == 2:
        return (M[0][0]*M[1][1]) - M[0][1]*M[1][0]
    
    D = 0
    for i in range(size[0]):
        M2 = copy.deepcopy(M)
        v = M2[0][i]
        M2.pop(0)
        M2 = transpose(M2)
        M2.pop(i)
        M2 = transpose(M2)
        D += v * det(M2) * (-1)**i
    return D

M1 = [
    [1,2,7,4],
    [5,7,7,8],
    [9,10,17,12],
    [13,14,15,17]
    ]
M2 = scale(2, M1)
M3 = [
    [5,6],
    [8,9],
    ]

#print(scale(2, M1))
#print(add(M1, M2))
#print(transpose(M3))
#print(multiply(M1, M3))
print(det(M1))
