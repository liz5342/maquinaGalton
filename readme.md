# Simulación de la Máquina de Galton

## Descripción

Este programa simula una máquina de Galton utilizando Python. La máquina de Galton es un dispositivo que demuestra el concepto de distribución normal a través de la caída de canicas a través de una serie de obstáculos. En este caso, el programa simula 3000 canicas cayendo a través de 12 niveles de obstáculos y luego grafica un histograma que muestra la cantidad de canicas en cada contenedor final.

## Características del Programa

1. **Simulación de la Máquina de Galton:**
   - La máquina tiene 12 niveles de obstáculos.
   - Cada canica tiene una probabilidad del 50% de moverse a la izquierda o a la derecha en cada nivel.
   - Se simulan 3000 canicas en total.

2. **Funciones del Programa:**
   - `simular_maquina_galton(num_canicas, num_niveles)`: Simula el recorrido de las canicas y devuelve una lista con la cantidad de canicas en cada contenedor.
   - `graficar_histograma(resultados)`: Genera un histograma utilizando `matplotlib` para visualizar los resultados de la simulación.

## Código

```python
import random
import matplotlib.pyplot as plt

def simular_maquina_galton(num_canicas, num_niveles):
    resultados = [0] * (num_niveles + 1)
    
    for _ in range(num_canicas):
        posicion = 0
        for _ in range(num_niveles):
            if random.random() < 0.5:
                posicion += 1
        resultados[posicion] += 1
    
    return resultados

def graficar_histograma(resultados):
    niveles = range(len(resultados))
    
    plt.bar(niveles, resultados, color='blue')
    plt.xlabel('Contenedores')
    plt.ylabel('Cantidad de Canicas')
    plt.title('Simulación de la Máquina de Galton')
    plt.show()

# Parámetros de la simulación
num_canicas = 3000
num_niveles = 12

# Realizar la simulación
resultados = simular_maquina_galton(num_canicas, num_niveles)

# Graficar el histograma
graficar_histograma(resultados)

