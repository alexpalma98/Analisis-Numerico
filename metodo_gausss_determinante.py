# Determinante de una matriz A
# convirtiendo a diagonal superior 

import numpy as np

# INGRESO
A = np.array([[3. , -0.1, -0.2],
              [0.1,  7. , -0.3],
              [0.3, -0.2, 10.  ]])

# PROCEDIMIENTO

# Matriz aumentada
AB = np.copy(A)

# Pivoteo parcial por filas

cambiofila = 0  # contador

tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]
# Para cada fila en AB
for i in range(0,n-1,1):
    # columna desde diagonal i en adelante
    columna  = abs(AB[i:,i])
    dondemax = np.argmax(columna)
    # dondemax no está en diagonal
    if (dondemax !=0):
        # intercambia filas
        
        cambiofila = cambiofila +1
        
        temporal = np.copy(AB[i,:])
        AB[i,:]  = AB[dondemax+i,:]
        AB[dondemax+i,:] = temporal
AB1 = np.copy(AB)

# eliminación hacia adelante
for i in range(0,n-1,1):
    pivote   = AB[i,i]
    adelante = i + 1
    for k in range(adelante,n,1):
        factor  = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor

# calcula determinante
multiplica = 1
for i in range(0,n,1):
    multiplica = multiplica*AB[i,i]
determinante = ((-1)**cambiofila)*multiplica

# SALIDA
print('Pivoteo parcial por filas')
print(AB1)
print('eliminación hacia adelante')
print(AB)
print('determinante: ')
print(determinante)
