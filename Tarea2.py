#Esta es la Tarea 2.10

#Una forma de calcular la probabilidad es usando la combinatoria

from scipy.special import comb

verdad = comb(50,10) # Las distintas formas de escoger 10 personas que siempre dicen la verdad
mentiras = comb(30,10) # Las distintas formas de escoger 10 personas que siempre mienten
no_responde = comb(20,10) # Las distintas formas de escoger 10 personas que se niegan a responder
total = comb(100,30) # Las maneras de escoger 30 personas de una aldea de 100 personas

probabilidad = (verdad*mentiras*no_responde)/total

print("La probabilidad de que se obtenga 10 personas de cada categoria es ", probabilidad)

#La otra forma es hacer una simulación estilo Monte Carlo

import random

def unir1(color, numero):
    return {color + str(n + 1) for n in range(numero)}

aldea = list(unir1('V', 50) | unir1('M', 30) | unir1('N', 20)) # Aquí se crea la urna con las 50 

muestra = {tuple(random.choices(aldea, k = 30)) for i in range(20000000)} # Se escogió ese rango porque más allá de eso ocupa toda la memoria RAM

def categoria10(evento): #Esta función entrega la muestra que contenga 10 personas de cada categoría
    s = [i[0] for i in evento]
    return s.count('V') == 10 and s.count('M') == 10 and s.count('N') == 10

def prob(evento, espacio): # Función para calcular probabilidad
    return (len(evento & espacio)/len(espacio))

categoria = {e for e in muestra if categoria10(e)}
prob(categoria, muestra) # Aquí se entrega la probabilidad usando simulaciones

import matplotlib.pyplot as plt
import numpy as np

#En esta parte se grafica a cuanto tiende la probabilidad 

sims = 10
puntos = 500000
probs = np.zeros(sims)

for i in range(sims):
    muestra = {tuple(random.choices(aldea, k = 30)) for i in range(puntos)}
    categoria = {e for e in muestra if categoria10(e)}
    probs[i] = prob(categoria, muestra)

plt.plot(np.arange(sims), probs)

probs.mean() # Se imprime el promedio de las probabilidades

probs.std()/probs.mean()

abs(probabilidad - probs.mean())/probabilidad # Aqui se calcula el error de la probabilidad comparando el valor real con la obtenida en la simulación

# El error que se comete es muy grande porque existen 2.937233982161094e+25 maneras de escoger 30 personas de un total de 100, y una muestra de 20000000 sigue siendo muy pequeño para este problema.
