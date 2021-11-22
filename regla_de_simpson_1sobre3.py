# Integración: Regla Simpson 1/3
import numpy as np
import matplotlib.pyplot as plt

# INGRESO:
fx = lambda x: np.sqrt(x)*np.sin(x)

# intervalo de integración
a = 1
b = 3
tramos = 8

# PROCEDIMIENTO
# Tarea: validar tramos par

# Regla de Simpson 1/3
h = (b-a)/tramos
xi = a
area = 0
for i in range(0,tramos,2):
    deltaA = (h/3)*(fx(xi)+4*fx(xi+h)+fx(xi+2*h))
    area = area + deltaA
    xi = xi + 2*h

# SALIDA
print('tramos:', tramos)
print('Integral: ', area)


#Algoritmo con varios segmentos y h constante

#Usado cuando el intervalo a integrar tiene varios segmentos, cada segmento tiene dos tramos.
#Ejemplo para dos segmentos, cuatro tramos, semejante al usado en la gráfica. La simplificación es válida si h es constante.

# Integración: Regla Simpson 1/3
# Validar cantidad de tramos pares
import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx = lambda x: np.sqrt(x)*np.sin(x)

# intervalo de integración
a = 1
b = 3
tramos = 8

# Validar cantidad de tramos pares
esimpar = tramos%2
while (esimpar == 1):
    tramos = int(input('tramos es par: '))
    esimpar = tramos%2

# PROCEDIMIENTO
# Regla de Simpson 1/3, varios tramos
h = (b-a)/tramos
xi = a
# segmento por cada dos tramos
suma = fx(xi)
for i in range(0,tramos-2,2):
    xi = xi + h
    suma = suma + 4*fx(xi)
    xi = xi + h
    suma = suma + 2*fx(xi)
# último segmento
xi = xi + h
suma = suma + 4*fx(xi)
suma = suma + fx(b)
area = (h/3)*suma

# SALIDA
print('tramos: ', tramos)
print('Integral: ', area)



#REALIZAR ALGORITMO PARA LAS GRAFICAS

