#Esta tarea corresponde a la 4.5

import numpy as np
import matplotlib.pyplot as plt

#Si las variables no son idénticamente distribuidas, quiere decir que no todas pertenecen a la misma distribución

#Vamos a ocupar las distribuciones binomial y de Poisson, y haremos dos casos

#En el primer caso, los parámetros de las dos distribuciones se eligen de tal manera que las dos variables sean casi idénticas
variables_poisson = np.random.poisson(50, 10000)
variables_binomial = np.random.binomial(100,0.5,10000)

plt.title('Variables aleatorias Binomial (n=100, p=0.5) y Poisson ($\lambda = 50$)')
plt.hist(np.concatenate((variables_poisson,variables_binomial)), bins=100) #Aquí las dos variables se unen para formar una sola
plt.show() #Vemos que en este caso tiende a una distribución normal

#Ahora cambiamos los parámetros de la distribución Poisson. Este es el segundo caso

variables_poisson2 = np.random.poisson(25, 10000)

plt.title('Variables aleatorias Binomial (n=100, p=0.5) y Poisson ($\lambda = 25$)')
plt.hist(np.concatenate((variables_poisson2,variables_binomial)), bins=100)
plt.show() #Aqui el teorema del límite central falla
