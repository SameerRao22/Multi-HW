# Sameer Rao

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

M1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
M2 = scale(2, M1)
M3 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]

print(scale(2, M1))
print(add(M1, M2))
print(transpose(M3))
print(multiply(M1, M3))
