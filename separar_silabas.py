def separar_silabas(palabra):
    palabra = palabra.strip()
    if not len(palabra): return [""]
    if 1 == len(palabra): return [palabra]
    vocales = list("aeiouáéíóúAEIOUÁÉÍÓÚ")
    son_u = ["ch", "sh", "ll", "qu", "gr", "br", "cr", "dr", "fr", "kr", "pr", "rr", "tr", "bl", "cl", "fl", "pl", "tl", "gl"]
    for x in range(len(son_u)):
        palabra = palabra.replace(son_u[x], str(x))
    silabas = []
    silaba_actual = ""
    no_vocal = False#true si no hay vocal
    for x in palabra:
        if x in vocales:
            no_vocal = True
    if not no_vocal:
        return [palabra]

    silabas = []
    silaba_actual = ""
    palabra += ">>"
    for x in range(len(palabra)):
        if silaba_actual == "":
            silaba_actual += palabra[x]
        elif palabra[x] in vocales:
            silaba_actual += palabra[x]
        elif x != len(palabra)-1:
            if not palabra[x] in vocales and not palabra[x+1] in vocales:
                silaba_actual += palabra[x]
                silabas.append(silaba_actual)
                silaba_actual = ""
            else:#es consonante
                silabas.append(silaba_actual)
                silaba_actual = ""
                silaba_actual += palabra[x]

    for x in range(len(son_u)):
            for y in range(len(silabas)):
                silabas[y] = silabas[y].replace(str(x), son_u[x])
                silabas[y] = silabas[y].replace(">", "")

    return silabas

texto = open("palabras.txt", encoding="utf-8").read().splitlines()#esto es una lista

#Ejemplo de uso
import time
import random

#while True:
for x in range(len(texto)):
    time.sleep(1.5)
    palabra = texto[x]
    print(separar_silabas(palabra), len(separar_silabas(palabra)))
