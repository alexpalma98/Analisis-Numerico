# Solución usando Matrices L y U
# continuación de ejercicio anterior

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

# Resolver LY = B
B1  = np.transpose([B1])
AB =np.concatenate((L,B1),axis=1)

# sustitución hacia adelante
Y = np.zeros(n,dtype=float)
Y[0] = AB[0,n]
for i in range(1,n,1):
    suma = 0
    for j in range(0,i,1):
        suma = suma + AB[i,j]*Y[j]
    b = AB[i,n]
    Y[i] = (b-suma)/AB[i,i]

Y = np.transpose([Y])

# Resolver UX = Y
AB =np.concatenate((U,Y),axis=1)

# sustitución hacia atrás
ultfila = n-1
ultcolumna = m-1
X = np.zeros(n,dtype=float)

for i in range(ultfila,0-1,-1):
    suma = 0
    for j in range(i+1,ultcolumna,1):
        suma = suma + AB[i,j]*X[j]
    b = AB[i,ultcolumna]
    X[i] = (b-suma)/AB[i,i]

X = np.transpose([X])

# SALIDA
print('Pivoteo parcial por filas: AB')
print(AB1)
print('eliminación hacia adelante')
print('Matriz U: ')
print(U)
print('matriz L: ')
print(L)
print('B1 :')
print(B1)
print('Y Sustitución hacia adelante')
print(Y)
print('X Sustitución hacia atras')
print(X)
