# Polinomio interpolación
# Diferencias finitas avanzadas
# Tarea: Verificar tamaño de vectores,
#        verificar puntos equidistantes en x

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO , Datos de prueba
xi = np.array([0.10, 0.2, 0.3, 0.4])
fi = np.array([1.45, 1.6, 1.7, 2.0])

# PROCEDIMIENTO

# Tabla de Diferencias Finitas
titulo = ['i','xi','fi']
n = len(xi)
ki = np.arange(0,n,1)
tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
tabla = np.transpose(tabla)

# diferencias finitas vacia
dfinita = np.zeros(shape=(n,n),dtype=float)
tabla = np.concatenate((tabla,dfinita), axis=1)

# Calcula tabla, inicia en columna 3
[n,m] = np.shape(tabla)
diagonal = n-1
j = 3
while (j < m):
    # Añade título para cada columna
    titulo.append('df'+str(j-2))
    # cada fila de columna
    i = 0
    while (i < diagonal):
        tabla[i,j] = tabla[i+1,j-1]-tabla[i,j-1]
        i = i+1
    diagonal = diagonal - 1
    j = j+1

# POLINOMIO con diferencias Finitas avanzadas
# caso: puntos equidistantes en eje x
h = xi[1] - xi[0]
dfinita = tabla[0,3:]
n = len(dfinita)

# expresión del polinomio con Sympy
x = sym.Symbol('x')
polinomio = fi[0]
for j in range(1,n,1):
    denominador = np.math.factorial(j)*(h**j)
    factor = dfinita[j-1]/denominador
    termino = 1
    for k in range(0,j,1):
        termino = termino*(x-xi[k])
    polinomio = polinomio + termino*factor

# simplifica multiplicando entre (x-xi)
polisimple = polinomio.expand()

# polinomio para evaluacion numérica
px = sym.lambdify(x,polisimple)

# Puntos para la gráfica
muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = px(pxi)

# SALIDA
print('Tabla Diferencia Finita')
print([titulo])
print(tabla)
print('dfinita: ')
print(dfinita)
print('polinomio: ')
print(polinomio)
print('polinomio simplificado: ' )
print(polisimple)

# Gráfica
plt.plot(xi,fi,'o', label = 'Puntos')
##for i in range(0,n,1):
##    plt.axvline(xi[i],ls='--', color='yellow')
plt.plot(pxi,pfi, label = 'Polinomio')

plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Interpolación polinómica')
plt.show()

