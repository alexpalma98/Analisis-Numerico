# Algoritmo Posicion Falsa para raices
# busca en intervalo [a,b]
import numpy as np

# INGRESO
fx = lambda x: x**3 + 4*x**2 - 10

a = 1
b = 2
tolera = 0.001

# PROCEDIMIENTO
tramo = abs(b-a)
while not(tramo<=tolera):
    fa = fx(a)
    fb = fx(b)
    c = b - fb*(a-b)/(fa-fb)
    fc = fx(c)
    cambia = np.sign(fa)*np.sign(fc)
    if (cambia > 0):
        tramo = abs(c-a)
        a = c
    else:
        tramo = abs(b-c)
        b = c
raiz = c

# SALIDA
print(raiz)

#Algoritmo aumentado para mostrar la tabla de cálculos

# Algoritmo Posicion Falsa para raices
# busca en intervalo [a,b]
# tolera = error

import numpy as np

# INGRESO
fx = lambda x: x**3 + 4*(x**2) -10

a = 1
b = 2
tolera = 0.0001

# PROCEDIMIENTO
tabla = []
tramo = abs(b-a)
fa = fx(a)
fb = fx(b)
while not(tramo<=tolera):
    c = b - fb*(a-b)/(fa-fb)
    fc = fx(c)
    tabla.append([a,c,b,fa,fc,fb,tramo])
    cambio = np.sign(fa)*np.sign(fc)
    if cambio>0:
        tramo = abs(c-a)
        a = c
        fa = fc
    else:
        tramo = abs(b-c)
        b = c
        fb = fc
        
tabla = np.array(tabla)
ntabla = len(tabla)

# SALIDA
np.set_printoptions(precision=4)
for i in range(0,ntabla,1):
    print('iteración:  ',i)
    print('[a,c,b]:    ', tabla[i,0:3])
    print('[fa,fc,fb]: ', tabla[i,3:6])
    print('[tramo]:    ', tabla[i,6])

print('raiz:  ',c)
print('error: ',tramo)
