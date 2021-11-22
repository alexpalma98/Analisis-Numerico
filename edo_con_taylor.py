#Para simplificar los calculos se crea una función edo_taylor3t() 
#para encontrar  los valores para una cantidad de muestras distanciadas entre si h veces del punto inicial [x0,y0]

# EDO. Método de Taylor 3 términos 
# estima solucion para muestras separadas h en eje x
# valores iniciales x0,y0
# entrega arreglo [[x,y]]
import numpy as np

def edo_taylor3t(d1y,d2y,x0,y0,h,muestras):
    tamano = muestras + 1
    estimado = np.zeros(shape=(tamano,4),dtype=float)
    # incluye el punto [x0,y0]
    estimado[0] = [x0,y0,0,0]
    x = x0
    y = y0
    for i in range(1,tamano,1):
        estimado[i-1,2:]= [d1y(x,y),d2y(x,y)]
        y = y + h*d1y(x,y) + ((h**2)/2)*d2y(x,y)
        x = x+h
        estimado[i,0:2] = [x,y]
    return(estimado)
  
  #La función se puede usar en un programa que plantee resolver el problema propuesto:

# PROGRAMA PRUEBA
# Ref Rodriguez 9.1.1 p335 ejemplo.
# prueba y'-y-x+(x**2)-1 =0, y(0)=1

# INGRESO.
# d1y = y', d2y = y''
d1y = lambda x,y: y -x**2 + x + 1
d2y = lambda x,y: y -x**2 - x + 2
x0 = 0
y0 = 1
h = 0.1
muestras = 5

# PROCEDIMIENTO
puntos = edo_taylor3t(d1y,d2y,x0,y0,h,muestras)
xi = puntos[:,0]
yi = puntos[:,1]

# SALIDA
print('estimado[xi, yi, d1yi, d2yi]')
print(puntos)

#CALCULO DEL ERROR

# ERROR vs solución conocida
y_sol = lambda x: ((np.e)**x) + x + x**2

yi_psol = y_sol(xi)
errores = yi_psol - yi
errormax = np.max(np.abs(errores))

# SALIDA
print('Error máximo estimado: ',errormax)
print('entre puntos: ')
print(errores)

#Gráfica
#Para visualizar los resultados se usan los puntos estimados
#y muchos más puntos para la solución conocida en el intervalo de estudio. Con la gráfica se podrán observar las diferencias entre las soluciones encontradas.

# GRAFICA [a,b+2*h]
a = x0
b = h*muestras+2*h
muestreo = 10*muestras+2
xis = np.linspace(a,b,muestreo)
yis = y_sol(xis)

# Gráfica
import matplotlib.pyplot as plt
plt.plot(xis,yis, label='y conocida')
plt.plot(xi[0],yi[0],'o', color='r', label ='[x0,y0]')
plt.plot(xi[1:],yi[1:],'o', color='g', label ='y estimada')
plt.title('EDO: Solución con Taylor 3 términos')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

