#Tarea 5.1

import numpy as np
import matplotlib.pyplot as plt

# Definimos la función
def funcion(x):
    return 1 - np.cos(x) - np.sin(x)/x

# Escribimos el método de bisección
def biseccion(f, a, b, epsilon, N=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Esta multiplicación debe dar negativo")

    lista_errores = [] #Aquí se guardarán los errores
    for i in range(N):
        punto_medio = a + (b - a)/2
        error = abs(b - a)/2  
        lista_errores.append(error)

        if error < epsilon:
            return punto_medio, lista_errores

        if f(punto_medio) * f(a) < 0: #Esto quiere decir que el cero está en el intervalo [a, c]
            b = punto_medio  
        else:                         #Si no, entonces el cero está en el intervalo [c, b]
            a = punto_medio 

    print("No se encontró el cero después de", N, "iteraciones")

# Definimos los puntos a, b y la precisión
a = -6.5
b = -6
epsilon = 1e-8  #Este valor se puede modificar para ver distintos graficos

# Aquí se guarda el cero de la función y la lista con los errores
cero, errores = biseccion(funcion, a, b, epsilon)

# Necesitamos el número de iteraciones para graficar
iteraciones = len(errores)

#Cota teórica
cota = abs(a-b)/(2**(iteraciones))

# Y finalmente graficamos del error relativo en función de las iteraciones
plt.plot(errores, label='Error relativo', marker='o')
plt.yscale('log')
plt.xlabel('Número de iteraciones')
plt.ylabel('Error relativo')
plt.title('Error relativo v/s número de iteraciones')
plt.legend()
plt.grid()
plt.show()

print("\n")
print(f"Luego de {iteraciones} iteraciones, el cero de la función es {cero}")

if errores[len(errores)-1] <= cota:
    print(f"La cota teórica es {cota}, y es menor o igual al último error de la iteración")

#NOTA: 70