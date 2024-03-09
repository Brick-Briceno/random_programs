import csv
import os

def escribir_en_celda(nombre_archivo, fila, columna, valor):
    # Verifica si el archivo existe
    if not os.path.exists(nombre_archivo):
        # Si no existe, crea el archivo y escribe una fila vacía
        with open(nombre_archivo, 'w', newline='') as archivo:
            escritor = csv.writer(archivo, delimiter='\t')
            escritor.writerow([])

    # Lee el archivo existente
    with open(nombre_archivo, 'r', newline='') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        filas = list(lector)

    # Asegúrate de que haya suficientes filas
    while len(filas) <= fila:
        filas.append([])

    # Asegúrate de que haya suficientes columnas en la fila específica
    while len(filas[fila]) <= columna:
        filas[fila].append('')

    # Modifica el valor en la fila y columna especificadas
    filas[fila][columna] = valor

    # Escribe los cambios de vuelta al archivo
    with open(nombre_archivo, 'w', newline='') as archivo:
        escritor = csv.writer(archivo, delimiter='\t')
        escritor.writerows(filas)

def leer_celda_en_archivo_tsv(nombre_archivo, fila, columna):
    try:
        with open(nombre_archivo, 'r', newline='') as archivo:
            lector = csv.reader(archivo, delimiter='\t')
            filas = list(lector)

            # Verifica que la fila y columna estén dentro de los límites
            if 0 <= fila < len(filas) and 0 <= columna < len(filas[fila]):
                return filas[fila][columna]
            else:
                print("Índices de fila y/o columna fuera de rango.")
                return None
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        return None

import csv
import os

def eliminar_fila(nombre_archivo, fila):
    # Verifica si el archivo existe
    if not os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' no existe.")
        return

    # Lee el archivo existente
    with open(nombre_archivo, 'r', newline='') as archivo:
        lector = csv.reader(archivo, delimiter='\t')
        filas = list(lector)

    # Verifica si la fila está dentro del rango de filas del archivo
    if 0 <= fila < len(filas):
        # Elimina la fila específica del archivo
        filas.pop(fila)

        # Escribe los cambios de vuelta al archivo
        with open(nombre_archivo, 'w', newline='') as archivo:
            escritor = csv.writer(archivo, delimiter='\t')
            escritor.writerows(filas)
    else:
        print("Índice de fila fuera de rango.")

# Ejemplo de uso:
eliminar_fila("ejemplo.tsv", 0)

for x in range(3):
    #Ejemplo de uso
    #escribir_en_celda('ejemplo.tsv', fila=x, columna=2, valor='XD')

    #Ejemplo de uso
    valor_celda = leer_celda_en_archivo_tsv('ejemplo.tsv', fila=x, columna=2)
    print(f"El valor en la celda ({x}, 2) es: {valor_celda}")
