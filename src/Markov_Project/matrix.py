def transpose(M):
    T = []
    for j in range(len(M[0])):
        temp = []
        for k in range(len(M)):
            temp.append(M[k][j])
        T.append(temp)
    return T

def dotProduct(V1, V2):
    S = 0
    for i in range(len(V1)):
        S += V1[i]*V2[i]
    return S

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