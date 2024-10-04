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

import numpy as np

simulaciones = 100000
personas_v = 50  #Personas que dicen la verdad
personas_m = 30  #Persoans que mienten
personas_n = 20  #Personas que se niegan a responder

def crear_simulacion(): # Esta función crea una simulación donde las muestras son de tamaño 30 y se verifica si contiene 10 personas de cada categoria
    poblacion = ['V'] * personas_v + ['M'] * personas_m + ['N'] * personas_n
    muestra = np.random.choice(poblacion, size=30, replace=False)
    verdades = np.sum(muestra == 'V')
    mentiras = np.sum(muestra == 'M')
    no_responde = np.sum(muestra == 'N')
    return (verdades == 10) and (mentiras == 10) and (no_responde == 10)

simulacion = [crear_simulacion() for i in range(simulaciones)]

probabilidad_promedio = np.mean(simulacion) #Aquí se calcula el promedio de la probabilidad de la simulación
print('Según las', simulaciones,' simulaciones, la probabilidad de que la muestra contenga 10 personas de cada categoria es', probabilidad_promedio)

error = abs(probabilidad - probabilidad_promedio)/probabilidad #Error que se comete cuando se compara la probabilidad real con la de la simulación 
print('Se comete un error de',"%.2f" % (error*100),'%')

#Nota: 70, mandar las tareas en un jupyter notebook por favor.