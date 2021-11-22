# 1ra Evaluación II Término 2011
# Tema 2. Sistema de ecuaciones 3x3
# Concepto como interseccion de Planos

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# INGRESO Ax=B
A = np.array([[-2, 5, 9],
              [ 7, 1, 1],
              [-3, 7,-1]])

B = np.array([1,6,-26])

ax = -5     # Intervalo X
bx = 5
ay = ax-2   # Intervalo Y
by = bx+2

muestras = 11

# PROCEDIMIENTO --------
# Ecuaciones de planos
z0 = lambda x,y: (-A[0,0]*x - A[0,1]*y + B[0])/A[0,2]
z1 = lambda x,y: (-A[1,0]*x - A[1,1]*y + B[1])/A[1,2]
z2 = lambda x,y: (-A[2,0]*x - A[2,1]*y + B[2])/A[2,2]

xi = np.linspace(ax,bx, muestras)
yi = np.linspace(ay,by, muestras)
Xi, Yi = np.meshgrid(xi,yi)

Z0 = z0(Xi,Yi)
Z1 = z1(Xi,Yi)
Z2 = z2(Xi,Yi)

# solución al sistema
punto = np.linalg.solve(A,B)

# SALIDA
print('respuesta de A.X=B : ')
print(punto)

# Interseccion entre ecuacion 1 y 2
# PlanoXZ, extremo inferior de y
Aa  = np.copy(A[0:2,[0,2]])
Ba  = np.copy(B[0:2])
Ba  = Ba-ay*A[0:2,1]
pta = np.linalg.solve(Aa,Ba)
pa  = np.array([ay])
pxza = np.array([pta[0],ay,pta[1]])

# PlanoXZ, extremo superior de y
Ba  = Ba-by*A[0:2,1]
ptb = np.linalg.solve(Aa,Ba)
pb  = np.array([by])
pxzb = np.array([ptb[0],by,ptb[1]])

# GRAFICA de planos
figura = plt.figure()
grafica = figura.add_subplot(111, projection='3d')

grafica.plot_wireframe(Xi,Yi,Z0,
                       color ='blue',
                       label='Ecuación 1')
grafica.plot_wireframe(Xi,Yi,Z1,
                       color ='green',
                       label='Ecuación 2')
grafica.plot_wireframe(Xi,Yi,Z2,
                       color ='orange',
                       label='Ecuación 3')
# recta intersección planos 1 y 2
grafica.plot([pxza[0],pxzb[0]],
             [pxza[1],pxzb[1]],
             [pxza[2],pxzb[2]],
             label='Sol 1y2',
             color = 'violet',
             linewidth = 4)
# Punto solución del sistema 3x3
grafica.scatter(punto[0],punto[1],punto[2],
                color = 'red',
                marker='o',
                label ='punto',
                linewidth = 6)

grafica.set_title('Sistema de ecuaciones 3x3')
grafica.set_xlabel('x')
grafica.set_ylabel('y')
grafica.set_zlabel('z')
grafica.legend()
grafica.view_init(45, 45)
# rotacion de ejes
for angulo in range(45, 360+45, 5 ):
    grafica.view_init(45, angulo)
    plt.draw()
    plt.pause(.001)
plt.show()
