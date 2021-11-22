# Pivoteo parcial por filas
# Solución a Sistemas de Ecuaciones

import numpy as np

# INGRESO
A = np.array([[4,2,5],
              [2,5,8],
              [5,4,3]])

B = np.array([[60.70],
              [92.90],
              [56.30]])

# PROCEDIMIENTO
# Matriz aumentada
AB  = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

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
        AB[i,:]  = AB[dondemax+i,:]
        AB[dondemax+i,:] = temporal

# SALIDA
print('Matriz aumentada:')
print(AB0)
print('Pivoteo parcial por filas')
print(AB)



#FUNCION PIVOTEA FILA M

def pivoteafila(M):
    '''
    Pivotea parcial por filas
    Si hay ceros en diagonal es matriz singular,
    Tarea: Revisar si diagonal tiene ceros
    '''
    # Pivoteo por filas AB
    tamano = np.shape(M)
    n = tamano[0]
    m = tamano[1]
    
    # Para cada fila en AB
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna = np.abs(M[i:,i])
        dondemax = np.argmax(columna)
        
        # dondemax no es en diagonal
        if (dondemax != 0):
            # intercambia filas
            temporal = np.copy(M[i,:])
            M[i,:] = M[dondemax+i,:]
            M[dondemax+i,:] = temporal
    return(M)
