# Ecuaciones Diferenciales Parciales
# Elipticas. Método iterativo
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
dx = 0.25 
dy = 0.25 
maxitera = 100
tolera = 0.0001

# PROCEDIMIENTO
xi = np.arange(x0,xn+dx,dx)
yj = np.arange(y0,yn+dy,dy)
n = len(xi)
m = len(yj)
# Matriz u
u = np.zeros(shape=(n,m),dtype = float)
# valores en fronteras
u[0,:]   = Ta
u[n-1,:] = Tb
u[:,0]   = Tc
u[:,m-1] = Td

# valor inicial de iteración
promedio = (Ta+Tb+Tc+Td)/4
u[1:n-1,1:m-1] = promedio
# iterar puntos interiores
itera = 0
converge = 0
while not(itera>=maxitera or converge==1):
    itera = itera +1
    nueva = np.copy(u)
    for i in range(1,n-1):
        for j in range(1,m-1):
            u[i,j] = (u[i-1,j]+u[i+1,j]+u[i,j-1]+u[i,j+1])/4
    diferencia = nueva-u
    erroru = np.linalg.norm(np.abs(diferencia))
    if (erroru<tolera):
        converge = 1

# SALIDA
np.set_printoptions(precision=2)
print('converge = ', converge)
print('xi=')
print(xi)
print('yj=')
print(yj)
print('matriz u')
print(u)


#La gráfica de resultados requiere ajuste de ejes, pues el índice de filas es el eje x, y las columnas es el eje y. 
#La matriz graficada se obtiene como la transpuesta de u

# Gráfica
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

X, Y = np.meshgrid(xi, yj)
U = np.transpose(u) # ajuste de índices fila es x

figura = plt.figure()
ax = Axes3D(figura)
ax.plot_surface(X, Y, U,
                rstride=1,
                cstride=1,
                cmap=cm.Reds)

plt.title('EDP elíptica')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

