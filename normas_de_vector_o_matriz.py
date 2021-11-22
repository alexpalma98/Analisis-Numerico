# Normas vectoriales y matriciales
# Referencia: Chapra 10.3, p299, pdf323
import numpy as np

def norma_p(X,p):
    Xp = (np.abs(X))**p
    suma = np.sum(Xp)
    norma = suma**(1/p)
    return(norma)

def norma_euclidiana(X):
    norma = norma_p(X,2)
    return(norma)

def norma_filasum(X):
    sfila = np.sum(np.abs(X),axis=1)
    norma = np.max(sfila)
    return(norma)

def norma_frobenius(X):
    tamano = np.shape(X)
    n = tamano[0]
    m = tamano[1]
    norma = 0
    for i in range(0,n,1):
        for j in range(0,m,1):
            norma =  norma + np.abs(X[i,j])**2
    norma = np.sqrt(norma)
    return(norma)

def num_condicion(X):
    M = np.copy(X)
    Mi = np.linalg.inv(M)
    nM = norma_filasum(M)
    nMi= norma_filasum(Mi)
    ncondicion = nM*nMi
    return(ncondicion)

# Programa de prueba #######
# INGRESO
A = np.array([[3,-0.1,-0.2],
              [0.1,7,-0.3],
              [0.3,-0.2,10]])

B = np.array([7.85,-19.3,71.4])

p = 2

# PROCEDIMIENTO
normap    = norma_p(B, p)
normaeucl = norma_euclidiana(B)
normafilasuma   = norma_filasum(A)
numerocondicion = num_condicion(A)

# SALIDA
print('vector:',B)
print('norma p: ',2)
print(normap)

print('norma euclididana: ')
print(normaeucl)

print('******')
print('matriz: ')
print(A)
print('norma suma fila: ',normafilasuma)

print('número de condición:')
print(numerocondicion)
