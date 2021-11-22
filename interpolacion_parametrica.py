# interpolación paramétrica
import numpy as np
import matplotlib.pyplot as plt

# INGRESO
ti = [0,1,2,3]
xti = [2,1,3,4]
yti = [0,4,5,0]

# PROCEDIMIENTO
# interpolando con lagrange
px = lambda t: (-2/3)*(t**3) + (7/2)*(t**2) + (-23/6)*t + 2
py = lambda t: (-1/2)*(t**3) + (9/2)*t

t = np.arange(0,3,0.01)
puntosx = px(t)
puntosy = py(t)

# Salida
plt.plot(puntosx,puntosy)
plt.show()

