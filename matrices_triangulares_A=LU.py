# Matrices L y U
# Modificando el método de Gauss

import numpy as np

# INGRESO
A = np.array([[ 3. , -0.1, -0.2],
              [ 0.1,  7. , -0.3],
              [ 0.3, -0.2, 10. ]], dtype=float)

B = np.array([7.85,-19.3,71.4], dtype=float)

# PROCEDIMIENTO
B  = np.transpose([B])
AB = np.concatenate((A,B),axis=1)
AB = np.copy(AB)

# Pivoteo parcial por filas
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

# Para cada fila en AB
for i in range(0,n-1,1):

    # columna desde diagonal i en adelante
    columna = abs(AB[i:,i])
    dondemax = np.argmax(columna)

    # dondemax no está en diagonal
    if (dondemax !=0):
        # intercambia filas
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[dondemax+i,:]
        AB[dondemax+i,:] = temporal

AB1 = np.copy(AB)
A1 = np.copy(AB[:,:m-1])
B1 = np.copy(AB[:,m-1])

# eliminacion hacia adelante
# se inicializa L
L = np.identity(n,dtype=float)
for i in range(0,n-1,1):
    pivote = AB[i,i]
    adelante = i+1
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
        L[k,i] = factor

U = np.copy(AB[:,:m-1])

# SALIDA
print('Pivoteo parcial por filas')
print(AB1)
print('eliminación hacia adelante')
print('Matriz U: ')
print(U)
print('matriz L: ')
print(L)

#Si se requiere una respuesta unificada en una variable, se puede convertir en una arreglo de matrices [L,U].
#Las matrices L y U se pueden leer como L=LU[0] y U=LU[1]


LU = np.array([L,U])

# SALIDA
print('triangular inferior L')
print(LU[0])
print('triangular superior U')
print(LU[1])
