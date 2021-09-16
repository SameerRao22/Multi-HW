# Sameer Rao
import copy
import matplotlib.pyplot as plt

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

#calculates determinant
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

def mPrint(M):
    for i in M:
        s = ""
        for j in i:
            if j == 0:
                j = abs(j)
            j = "{:.3f}".format(j)
            s += str(j).ljust(10) 
        print(s)

#transforms a vector V using a matrix M
def transform(M, V):
  plt.style.use('dark_background')
  plt.plot(V[0],V[1],'magenta')
  V2 = multiply(M,V)
  plt.plot(V2[0],V2[1],'cyan')
  plt.show()

def rowSwap(M, r1, r2):
    v = M[r1]
    M[r1] = M[r2]
    M[r2] = v

def rowScale(M, r1, s):
    for i in range(len(M[0])):
        M[r1][i] *= s

def rowSum(M, r1, r2, s):
    for i in range(len(M[0])):
        M[r2][i] += s*M[r1][i]

def zeros(M):
    z = []
    for i in range(len(M)):
        flag = True
        for j in range(len(M[0])):
            if M[i][j] != 0:
                flag = False
        if flag:
            z.append(i)
    return z

def rref(M):
    M = copy.deepcopy(M)
    allZero = True
    for i in range(len(M)):
        for j in range(len(M[0])):
                if M[i][j] != 0:
                    allZero = False
                    break
    if allZero:
        return M
    i = 1
    while (M[0][0] == 0):
       rowSwap(M, 0, i)
       i+=1
   
    rowScale(M, 0, 1./M[0][0])
    
    v = len(M)
    if len(M) > len(M[0]):
        v = len(M[0])

    for r in range(v):
        for i in range(v):
            if (i == r):
                continue
            if (M[r][r] != 0):
                rowSum(M, r, i, (M[i][r]*-1)/(M[r][r]))
   
    z = zeros(M)
    z.sort(reverse=True)
    last = len(M)
    for i in range(len(z)):
        last -= 1
        rowSwap(M, z[i], last)
    return M

def identity(n):
    I = []
    for j in range(n):
      R = []
      for k in range(n):
        if j == k:
          R.append(1)  
        else:
          R.append(0)
      I.append(R)
    return I

def inverse(M):
  M2 = copy.deepcopy(M)
  I = identity(len(M2))
  for j in range(len(M2)):
    for k in range(len(M2)):
      M2[j].append(I[j][k])
  M2 = rref(M2)
  
  N = []
  for j in range(len(M)):
    R = []
    for k in range(len(M)):
      R.append(M2[j][k+len(M)])
    N.append(R)
  return N

def solve(M, b):
    M = copy.deepcopy(M)
    M = inverse(M)
    x = multiply(M, b)
    return x
