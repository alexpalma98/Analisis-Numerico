# Norma como error
# o distancia entre dos puntos
# caso 3D
import numpy as np

# INGRESO
X0 = np.array([0.0, 0, 0])
X1 = np.array([1.0, 2, 3])
X2 = np.array([2.0, 4,-1])

# PROCEDIMIENTO
errado = X1 - X2
distancia = np.sqrt(np.sum(errado**2))
# funciones numpy
Nerrado = np.linalg.norm(errado)

# SALIDA
print('X1 = ', X1)
print('X2 = ', X2)
print('errado = ', errado)
print('||errado|| = ', distancia)
print('Norma euclidiana : ',Nerrado)


# Grafica
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
figura  = plt.figure()
grafica = figura.add_subplot(111,projection = '3d')

# puntos en el espacio
[x, y , z] = X0
grafica.scatter(x,y,z, c = 'blue',
                marker='o', label = 'X0')

[x, y , z] = X1
grafica.scatter(x,y,z, c = 'red',
                marker='o', label = 'X1')

[x, y , z] = X2
grafica.scatter(x,y,z, c = 'green',
                marker='o', label = 'X2')

# líneas entre puntos
linea = np.concatenate(([X0],[X1]),axis = 0)
x = linea[:,0]
y = linea[:,1]
z = linea[:,2]
grafica.plot(x,y,z, label = '||X1||')

linea = np.concatenate(([X0],[X2]),axis = 0)
x = linea[:,0]
y = linea[:,1]
z = linea[:,2]
grafica.plot(x,y,z, label = '||X2||')

linea = np.concatenate(([X1],[X2]),axis = 0)
x = linea[:,0]
y = linea[:,1]
z = linea[:,2]
grafica.plot(x,y,z, label = '||error||')

grafica.set_xlabel('eje x')
grafica.set_ylabel('eje y')
grafica.set_zlabel('eje z')
grafica.legend()

grafica.view_init(35, 25)
plt.show()
