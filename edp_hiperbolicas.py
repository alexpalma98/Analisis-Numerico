# Ecuaciones Diferenciales Parciales
# Hiperbólica. Método explicito
import numpy as np

def cuerdainicio(xi):
    n = len(xi)
    y = np.zeros(n,dtype=float)
    for i in range(0,n,1):
        if (xi[i]<=0.5):
            y[i]=-0.5*xi[i]
        else:
            y[i]=0.5*(xi[i]-1)
    return(y)

# INGRESO
x0 = 0
xn = 1 # Longitud de cuerda
y0 = 0
yn = 0 # Puntos de amarre
t0 = 0
c = 2
# discretiza
tramosx = 16
tramost = 32
dx = (xn-x0)/tramosx 
dt = dx/c

# PROCEDIMIENTO
xi = np.arange(x0,xn+dx,dx)
tj = np.arange(0,tramost*dt+dt,dt)
n = len(xi)
m = len(tj)

u = np.zeros(shape=(n,m),dtype=float)
u[:,0] = cuerdainicio(xi)
u[0,:] = y0
u[n-1,:] = yn
# Aplicando condición inicial
j = 0
for i in range(1,n-1,1):
    u[i,j+1] = (u[i+1,j]+u[i-1,j])/2
# Para los otros puntos
for j in range(1,m-1,1):
    for i in range(1,n-1,1):
        u[i,j+1] = u[i+1,j]-u[i,j-1]+u[i-1,j]

# SALIDA
np.set_printoptions(precision=2)
print('xi =')
print(xi)
print('tj =')
print(tj)
print('matriz u =')
print(u)


#con lo que se obtienen los resultados numéricos, que para mejor interpretación se presentan en una gráfica estática y otra animada.

# GRAFICA
import matplotlib.pyplot as plt

for j in range(0,m,1):
    y = u[:,j]
    plt.plot(xi,y)

plt.title('EDP hiperbólica')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# **** GRÁFICO CON ANIMACION ***********
import matplotlib.animation as animation

# Inicializa parametros de trama/foto
retardo = 70   # milisegundos entre tramas
tramas  = m
maximoy = np.max(np.abs(u))
figura, ejes = plt.subplots()
plt.xlim([x0,xn])
plt.ylim([-maximoy,maximoy])

# lineas de función y polinomio en gráfico
linea_poli, = ejes.plot(xi,u[:,0], '-')
plt.axhline(0, color='k')  # Eje en x=0

plt.title('EDP hiperbólica')
# plt.legend()
# txt_x = (x0+xn)/2
txt_y = maximoy*(1-0.1)
texto = ejes.text(x0,txt_y,'tiempo:',
                  horizontalalignment='left')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

# Nueva Trama
def unatrama(i,xi,u):
    # actualiza cada linea
    linea_poli.set_ydata(u[:,i])
    linea_poli.set_xdata(xi)
    linea_poli.set_label('tiempo linea: '+str(i))
    texto.set_text('tiempo['+str(i)+']')
    # color de la línea
    if (i<=9):
        lineacolor = 'C'+str(i)
    else:
        numcolor = i%10
        lineacolor = 'C'+str(numcolor)
    linea_poli.set_color(lineacolor)
    return linea_poli, texto

# Limpia Trama anterior
def limpiatrama():
    linea_poli.set_ydata(np.ma.array(xi, mask=True))
    linea_poli.set_label('')
    texto.set_text('')
    return linea_poli, texto

# Trama contador
i = np.arange(0,tramas,1)
ani = animation.FuncAnimation(figura,
                              unatrama,
                              i ,
                              fargs=(xi,u),
                              init_func=limpiatrama,
                              interval=retardo,
                              blit=True)
# Graba Archivo video y GIFAnimado :
# ani.save('EDP_hiperbólica.mp4')
ani.save('EDP_hiperbolica.gif', writer='imagemagick')
plt.draw()
plt.show()



#Una vez realizado el algoritmo, se pueden cambiar las condiciones iniciales de la cuerda y se observan los resultados.
