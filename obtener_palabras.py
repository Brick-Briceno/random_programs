#Algoritmo que guarda palabras en una lista
import os
ruta_carpeta = "data_set_textos"
nombres_archivos = os.listdir(ruta_carpeta)
texto = ""

print("""Como usar???

1. Crea una capeta al lado de este programa llamada "data_set_textos"
2. mete desde archivos .txt o .str

""")

print("Procesando...")

for x in nombres_archivos:
    try:
        texto += open(ruta_carpeta + "\\" + x, encoding="utf-8").read() + "\n"
    except UnicodeDecodeError:
        texto += open(ruta_carpeta + "\\" + x, encoding="ansi").read() + "\n"
    except UnicodeDecodeError:
        print("Error de codificación del archivo: " + ruta_carpeta + "\\" + x)
        input("\npresione para Salir")
        quit()


def obtener_palabras(txt):
    palabra = ""
    lista_palabras = []
    letras = "abcdefghijklmnñopqrstuvwxyzáéíóú"
    cart = tuple(letras + letras.upper())#caracteres cart

    for x in range(len(txt)):
        if txt[x] in cart:
            palabra += txt[x]
        else:
            palabra = palabra.lower()
            if not palabra in lista_palabras:
                lista_palabras.append(palabra)
            palabra = ""
    #print("Hay", len(lista_palabras[1:]), "palabras")
    return lista_palabras[1:]

def txt_a_archivo(texto):
    with open("salida.txt", "a", encoding="utf-8") as archivo:
        archivo.write(texto + "\n")

print("Haciendo Orden Lexicográfico")
print(">>> Orden afabetico")
palabras = obtener_palabras(texto)
palabras = sorted(palabras)

print("Guardando...")

for y in nombres_archivos:
    for x in palabras:
        txt_a_archivo(x)
