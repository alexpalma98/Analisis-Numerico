# Integración: Cuadratura de Gauss de dos puntos
# modelo con varios tramos entre [a,b]
# para un solo segmento.
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import scipy.optimize as op

# INGRESO
x = sym.Symbol('x')

# fx = (x)**2
fx = x**2 + x + 1
# fx = 0.2 + 25.0*x-200*(x**2)+675.0*(x**3)-900.0*(x**4)+400.0*(x**5)

a = -1
b = 1
muestras = 51
tolera = 1e-12
iteramax = 100

# PROCEDIMIENTO
# Desarrollo analítico con Sympy
Fx = sym.integrate(fx,x)
Fxn = sym.lambdify('x',Fx,'numpy')
Fiab = Fxn(b)-Fxn(a)

# Busca igualar trapecio con Integral analitico
fxn = sym.lambdify('x',fx,'numpy')
base = b-a
mitad = base/2
xc = (a+b)/2  # centro
diferencia = lambda x: Fiab-base*(fxn(xc-x)+fxn(xc+x))/2
desplazado =  op.bisect(diferencia,0,mitad,
                        xtol=tolera,maxiter=iteramax)
factor = desplazado/mitad

# Integral aproximando con trapecio
x0 = xc - factor*mitad
x1 = xc + factor*mitad
Faprox = base*(fxn(x0)+fxn(x1))/2

# Integral cuadratura Gauss
xa = xc + mitad/np.sqrt(3)
xb = xc - mitad/np.sqrt(3)
FcuadG = base*(fxn(xa)+fxn(xb))/2
erradofactor = np.abs(FcuadG - Faprox)
erradoIntegral = np.abs(Fiab-Faprox)
# SALIDA
print('funcion  fx:  ', fx)
print('Integral Fx:  ', Fx)
print('I analitico:  ', Fiab)
print('I aproximado: ', Faprox)
print('desplaza centro:  ', desplazado)
print('factor desplaza:  ', factor)
print('Factor CuadGauss: ', 1/np.sqrt(3))
print('erradoFactor:   ', erradofactor)
print('error integral: ', erradoIntegral) 

# Grafica
# Para GRAFICAR 
# Para gráfica f(x)
xi = np.linspace(a,b,muestras)
fi = fxn(xi)

# Para gráfica Trapecio
m = (fxn(x1)-fxn(x0))/(x1-x0)
trapeciof = lambda x: fxn(x0)+m*(x-x0)
trapecioi = trapeciof(xi)

# Areas Trapecio para cada punto que busca
k = int(muestras/2)
xicg = xi[k:muestras-1]
Fcg = [base*(fxn(xi[k+0])+fxn(xi[k-0]))/2]
for i in range(1,k,1):
    untrapecio = base*(fxn(xi[k+i])+fxn(xi[k-i]))/2
    Fcg.append(untrapecio)

# Punto buscado
Fiaprox = base*(fxn(x1)+fxn(x0))/2

Fi = Fxn(xi)-Fxn(a)

# Areas de curvas y trapecio

plt.subplot(211) # Grafica superior
plt.xlim(a,b)
plt.plot(xi, fi, label='f(x)')
# Solo fi
# plt.fill_between(xi,0, fi,
#                label='integral fi',
#                 color='yellow')
# usando cuadratura
plt.fill_between(xi,0, trapecioi,
                 label='Cuadratura 2 puntos',
                 color='yellow')
plt.axvline(x0,color='white')
plt.axvline(x1,color='white')
plt.plot([x0,x1],[fxn(x0),fxn(x1)],
         'ro', label='x0,x1')
plt.axvline(0,color='black')
plt.xlabel('x')
plt.ylabel('f(x) y Cuadratura de 2 puntos')
plt.legend()

# Valores de integrales
plt.subplot(212) # Grafica inferior
plt.xlim(a,b)
plt.axhline(Fiab, label='F[a,b]')
# plt.plot(xi,Fi,label='F(x)')
plt.plot(xicg,Fcg,color='orange',label='Aprox Trapecio')

plt.axvline(x1,color='yellow')
plt.axvline((1/np.sqrt(3))*(b-a)/2 + xc ,color='magenta')
plt.plot(x1,Fiaprox,'ro', label='x0,x1')
plt.axvline(0,color='black')

plt.xlabel('x')
plt.legend()
plt.ylabel('Integrando')
plt.show()

