# EDP parabólicas d2u/dx2  = K du/dt
# método implícito
# Referencia: Chapra 30.3 p.895 pdf.917
#       Rodriguez 10.2.5 p.417
import numpy as np
import matplotlib.pyplot as plt

# INGRESO
# Valores de frontera
Ta = 60
Tb = 40
T0 = 25
# longitud en x
a = 0
b = 1
# Constante K
K = 4
# Tamaño de paso
dx = 0.1
dt = 0.01
# iteraciones en tiempo
n = 100

# PROCEDIMIENTO
# Valores de x
xi = np.arange(a,b+dx,dx)
m  = len(xi)
ultimox = m-1

# Resultados en tabla de u
u = np.zeros(shape=(m,n), dtype=float)
# valores iniciales de u[:,j]
j = 0
ultimot = n-1
u[0,j]= Ta
u[1:ultimox,j] = T0
u[ultimox,j] = Tb

# factores P,Q,R
lamb = dt/(K*dx**2)
P = lamb
Q = -1 -2*lamb
R = lamb

# Calcula U para cada tiempo + dt
j = 1
while not(j>=n):
    u[0,j] = Ta
    u[m-1,j] = Tb

    # Matriz de ecuaciones
    tamano = m-2
    A = np.zeros(shape=(tamano,tamano), dtype = float)
    B = np.zeros(tamano, dtype = float)
    for f in range(0,tamano,1):
        if (f>0):
            A[f,f-1]=P
        A[f,f] = Q
        if (f<(tamano-1)):
            A[f,f+1]=R
        B[f] = -u[f+1,j-1]
    B[0] = B[0]-P*u[0,j]
    B[tamano-1] = B[tamano-1]-R*u[m-1,j]
    # Resuelve sistema de ecuaciones
    C = np.linalg.solve(A, B)
    
    # copia resultados a u[i,j]
    for f in range(0,tamano,1):
        u[f+1,j] = C[f]

    # siguiente iteración
    j = j + 1
        
# SALIDA
print('Tabla de resultados')
np.set_printoptions(precision=2)
print(u)


#Para realizar la gráfica se aplica lo mismo que en el método explícito

# Gráfica
salto = int(n/10)
if (salto == 0):
    salto = 1
for j in range(0,n,salto):
    vector = u[:,j]
    plt.plot(xi,vector)
    plt.plot(xi,vector, '.m')

plt.xlabel('x[i]')
plt.ylabel('t[j]')
plt.title('Solución EDP parabólica')
plt.show()

