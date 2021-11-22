# Runge Kutta de 4do orden
def rungekutta4(d1y,x0,y0,h,muestras):
    tamano = muestras + 1
    estimado = np.zeros(shape=(tamano,2),dtype=float)
    
    # incluye el punto [x0,y0]
    estimado[0] = [x0,y0]
    xi = x0
    yi = y0
    for i in range(1,tamano,1):
        K1 = h * d1y(xi,yi)
        K2 = h * d1y(xi+h/2, yi + K1/2)
        K3 = h * d1y(xi+h/2, yi + K2/2)
        K4 = h * d1y(xi+h, yi + K3)

        yi = yi + (1/6)*(K1+2*K2+2*K3 +K4)
        xi = xi + h
        
        estimado[i] = [xi,yi]
    return(estimado)
  
  
  
