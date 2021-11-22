# Ecuaciones Diferenciales Parciales
# Elipticas. Método implícito
import numpy as np

# INGRESO
# Condiciones iniciales en los bordes
Ta = 60
Tb = 60
Tc = 50
Td = 70
# dimensiones de la placa
x0 = 0
xn = 2
y0 = 0
yn = 1.5
# discretiza, supone dx=dy
tramosx = 4
tramosy = 4
dx = (xn-x0)/tramosx 
dy = (yn-y0)/tramosy 
maxitera = 100
tolera = 0.0001

A = np.array([
    [-4, 1, 0, 1, 0, 0, 0, 0, 0],
    [ 1,-4, 1, 0, 1, 0, 0, 0, 0],
    [ 0, 1,-4, 0, 0, 1, 0, 0, 0],
    [ 1, 0, 0,-4, 1, 0, 1, 0, 0],
    [ 0, 1, 0, 1,-4, 1, 0, 1, 0],
    [ 0, 0, 1, 0, 1,-4, 0, 0, 1],
    [ 0, 0, 0, 1, 0, 0,-4, 1, 0],
    [ 0, 0, 0, 0, 1, 0, 1,-4, 1],
    [ 0, 0, 0, 0, 0, 1, 0, 1,-4],
    ])
B = np.array([-(Tc+Ta),-Tc,-(Tc+Tb),
              -Ta,0,-Tb,
              -(Td+Ta),-Td,-(Td+Tb)])


# PROCEDIMIENTO
# Resuelve sistema ecuaciones
Xu = np.linalg.solve(A,B)
[nx,mx] = np.shape(A)

xi = np.arange(x0,xn+dx,dx)
yj = np.arange(y0,yn+dy,dy)
n = len(xi)
m = len(yj)

u = np.zeros(shape=(n,m),dtype=float)
u[:,0]   = Tc
u[:,m-1] = Td
u[0,:]   = Ta
u[n-1,:] = Tb
u[1:1+3,1] = Xu[0:0+3]
u[1:1+3,2] = Xu[3:3+3]
u[1:1+3,3] = Xu[6:6+3]

# SALIDA
np.set_printoptions(precision=2)
print('xi=')
print(xi)
print('yj=')
print(yj)
print('matriz u')
print(u)

#GRAFICA

# Gráfica
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

X, Y = np.meshgrid(xi, yj)
U = np.transpose(u) # ajuste de índices fila es x

figura = plt.figure()
ax = Axes3D(figura)
ax.plot_surface(X, Y, U, rstride=1, cstride=1, cmap=cm.Reds)

plt.title('EDP elíptica')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
