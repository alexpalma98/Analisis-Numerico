# Integración: Regla de los trapecios
# Usando una función fx()
import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx = lambda x: np.sqrt(x)*np.sin(x)

# intervalo de integración
a = 1
b = 3
tramos = 4

# PROCEDIMIENTO
# Regla del Trapecio
# Usando tramos equidistantes en intervalo
h = (b-a)/tramos
xi = a
suma = fx(xi)
for i in range(0,tramos-1,1):
    xi = xi + h
    suma = suma + 2*fx(xi)
suma = suma + fx(b)
area = h*(suma/2)

# SALIDA
print('tramos: ', tramos)
print('Integral: ', area)



#La gráfica como ayuda didáctica, si la cantidad de tramos sea «poca»,
#muestra los trapecios, si aumenta la cantidad de tramos, no es necesario poner líneas verticales en blanco para separar los trapecios:

# GRAFICA
# Puntos de muestra
muestras = tramos + 1
xi = np.linspace(a,b,muestras)
fi = fx(xi)
# Linea suave
muestraslinea = tramos*10 + 1
xk = np.linspace(a,b,muestraslinea)
fk = fx(xk)

# Graficando
plt.plot(xk,fk, label ='f(x)')
plt.plot(xi,fi, marker='o',
         color='orange', label ='muestras')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Integral: Regla de Trapecios')
plt.legend()

# Trapecios
plt.fill_between(xi,0,fi, color='g')
for i in range(0,muestras,1):
    plt.axvline(xi[i], color='w')

plt.show()

#Para rellenar el área bajo la curva se usa la instrucción plt.fill_between(xi,0,fi, color=’g’). 
#La división de los trapecios con una línea blanca (white) se realiza con la instrucción plt.axvline(xi[i], color=’w’).

#Algoritmo con muestras
#Algoritmo usando las muestras y para tramos que pueden tener distancias arbitrarias. En este caso se usa la formula del área del trapecio para cada tramo.
#Usado para ejercicios donde los datos proporcionados son muestras. 
#Se adapta el bloque de ingreso y el procedimiento inicia desde «Regla de Trapecio». La cantidad de tramos será el numero de muestras menos uno tramos = len(xi) - 1


# Integración: Regla de los trapecios
# Usando incluso muestras arbitrariamente espaciadas
import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx = lambda x: np.sqrt(x)*np.sin(x)

# intervalo de integración
a = 1
b = 3
tramos = 4

# PROCEDIMIENTO
# Puntos de muestra
muestras = tramos + 1
xi = np.linspace(a,b,muestras)
fi = fx(xi)

# Regla del Trapecio
# Usando puntos muestreados
# incluso arbitrariamente espaciados
suma = 0
for i in range(0,tramos,1):
    dx = xi[i+1]-xi[i]
    Atrapecio = dx*(fi[i]+fi[i+1])/2
    suma = suma + Atrapecio
integral = suma

# SALIDA
print('tramos: ', tramos)
print('integral: ', integral)
