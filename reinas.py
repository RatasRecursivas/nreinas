#!/usr/bin/env python
from itertools import permutations
from math import fabs

# Determina si dos reinas se atacan en el tablero
def seatacan(reina1_x, reina1_y, reina2_x, reina2_y):
    if reina1_y == reina2_y:
        return True
    elif fabs(reina2_x - reina1_x) == fabs(reina2_y - reina1_y):
        return True
    else:
        return False

# Algoritmo de n reinas por fuerza bruta
def nreinas(n):
    # Genero las n! formas de poner las n reinas en el tablero
    total_soluciones = permutations([i for i in range(n)])
    soluciones = 0 # Contar la cantidad de soluciones, solo por diversion :)
    solucion  = True # Asumimos que la permutacion es valida (Toda persona es inocente hasta que se demuestre lo contrario)

    for permutacion in total_soluciones:
        # Esto esta medio tricky, checkea cada reina contra el resto, una especie de burbuja
        # Super lento
        for reina1_x, reina1_y in enumerate(permutacion):
            if not solucion: # Aca acortamos el trabajo, si el bucle de abajo pillo algun par de reinas amenazandose ya no es una solucion valida
                break
            for reina2_x, reina2_y in enumerate(permutacion[reina1_x + 1:], start = reina1_x + 1):
                if seatacan(reina1_x, reina1_y, reina2_x, reina2_y): # Si dos reinas se amenazan, cortamos este bucle y la variable de control la seteamos a falso
                    solucion = False
                    break
        if solucion: # Si ninguna reina se ataca tenemos una solucion valida!
            soluciones += 1
        solucion = True

    return soluciones
