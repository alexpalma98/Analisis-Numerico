# EDP parabólicas d2u/dx2  = K du/dt
# método explícito,usando diferencias divididas
# Referencia: Chapra 30.2 p.888 pdf.912
#       Rodriguez 10.2 p.406
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
dt = dx/10
# iteraciones en tiempo
n = 200

# PROCEDIMIENTO
# iteraciones en longitud
xi = np.arange(a,b+dx,dx)
m = len(xi)
ultimox = m-1

# Resultados en tabla u[x,t]
u = np.zeros(shape=(m,n), dtype=float)

# valores iniciales de u[:,j]
j=0
ultimot = n-1
u[0,:]= Ta
u[1:ultimox,j] = T0
u[ultimox,:] = Tb

# factores P,Q,R
lamb = dt/(K*dx**2)
P = lamb
Q = 1 - 2*lamb
R = lamb

# Calcula U para cada tiempo + dt
j = 0
while not(j>=ultimot): # igual con lazo for
    for i in range(1,ultimox,1):
        u[i,j+1] = P*u[i-1,j] + Q*u[i,j] + R*u[i+1,j]
    j=j+1

# SALIDA
print('Tabla de resultados')
np.set_printoptions(precision=2)
print(u)
      
  
#Si la cantidad de puntos aumenta al disminuir Δx y Δt, 
#es mejor disminuir la cantidad de curvas a usar en el gráfico para evitar superponerlas.
#Se usa el parámetro ‘salto’ para indicar cada cuántas curvas calculadas se incorporan en la gráfica.


# Gráfica
salto = int(n/10)
if (salto == 0):
    salto = 1
for j in range(0,n,salto):
    vector = u[:,j]
    plt.plot(xi,vector)
    plt.plot(xi,vector, '.r')
    
plt.xlabel('x[i]')
plt.ylabel('t[j]')
plt.title('Solución EDP parabólica')
plt.show()


# Gráfica
      
