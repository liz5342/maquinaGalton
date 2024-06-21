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
