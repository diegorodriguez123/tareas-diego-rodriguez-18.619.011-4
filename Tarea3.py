#Esta es la Tarea 3.5

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

# Este es un problema de distribución de Poisson

def poisson(n, lamda):
    return (lamda**n)*np.exp(-lamda)/factorial(n)

#De aquí se extrae un número aleatorio entre 0  y 1
num_aleatorio = np.random.random()

#Si se detectan 100 partículas en 60 segundos, entonces 100*10/60 partículas golpean el detector en 10 segundos
lamda = 100*10/60

n = 0 #Esta variable nos indicará la cantidad de partículas que es probable que ocurra dado por la variable num_aleatorio
probabilidad = poisson(n, lamda) # Esta probabilidad aumentará hasta que sea mayor que el número aleatorio entre 0 y 1
while probabilidad < num_aleatorio:
    n += 1
    probabilidad += poisson(n, lamda)

velocidades = np.random.normal(0.99, 0.01, n)  #Este es un arreglo que contiene las velocidades aleatorias de las n partículas

#Finalmente graficamos la distribución de las velocidades para ver cuál de ellas es más frecuente
plt.hist(velocidades, edgecolor='black')
plt.title('Distribución de velocidades de las partículas en 10 segundos')
plt.xlabel('Velocidad en términos de c')
plt.ylabel('Cantidad de eventos')
plt.grid(True)
