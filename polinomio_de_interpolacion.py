# El polinomio de interpolación
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO
xi = [0,0.2,0.3,0.4]
fi = [1,1.6,1.7,2.0]
# muestras = tramos+1
muestras = 101

# PROCEDIMIENTO
# Convierte a arreglos numpy 
xi = np.array(xi)
B = np.array(fi)
n = len(xi)

# Matriz Vandermonde D
D = np.zeros(shape=(n,n),dtype =float)
for i in range(0,n,1):
    for j in range(0,n,1):
        potencia = (n-1)-j # Derecha a izquierda
        D[i,j] = xi[i]**potencia

# Aplicar métodos Unidad03. Tarea
# Resuelve sistema de ecuaciones A.X=B
coeficiente = np.linalg.solve(D,B)

# Polinomio en forma simbólica
x = sym.Symbol('x')
polinomio = 0
for i in range(0,n,1):
    potencia = (n-1)-i   # Derecha a izquierda
    termino = coeficiente[i]*(x**potencia)
    polinomio = polinomio + termino

# Polinomio a forma Lambda
# para evaluación con vectores de datos xin
px = sym.lambdify(x,polinomio)

# Para graficar el polinomio en [a,b]
a = np.min(xi)
b = np.max(xi)
xin = np.linspace(a,b,muestras)
yin = px(xin)

# Usando evaluación simbólica
##yin = np.zeros(muestras,dtype=float)
##for j in range(0,muestras,1):
##    yin[j] = polinomio.subs(x,xin[j])
    
# SALIDA
print('Matriz Vandermonde: ')
print(D)
print('los coeficientes del polinomio: ')
print(coeficiente)
print('Polinomio de interpolación: ')
print(polinomio)
print('\n formato pprint')
sym.pprint(polinomio)

# Grafica
plt.plot(xi,fi,'o', label='[xi,fi]')
plt.plot(xin,yin, label='p(x)')
plt.xlabel('xi')
plt.ylabel('fi')
plt.legend()
plt.title(polinomio)
plt.show()
