import os
from collections import Counter

input("leyendo todos los archivos de texto en la carpeta \"data_set_textos\"")
folder_path = "data_set_textos"
all_text = ""
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), "rb") as file:
            try:
                content = file.read().decode("utf-8")
            except UnicodeDecodeError:
                content = file.read().decode("ansi", errors="ignore")
            all_text += content + "\n"

#Crear la lista de caracteres permitidos
caracteres = "abcdefghijklmnopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ"

input("Extraer palabras del texto y eliminar signos de puntuación y números")
words = []
word = ""
for char in all_text:
    if char in caracteres:
        word += char
    else:
        if word:
            words.append(word)
            word = ""
if word:
    words.append(word)

input("Convertir todo a minúsculas y contar la frecuencia de las palabras")
word_counter = Counter([word.lower() for word in words])

input("Ordenar las palabras por frecuencia")
sorted_words = sorted(word_counter, key=lambda word: word_counter[word], reverse=True)

input("Guardar las palabras únicas en un archivo de texto")
output_file = "palabras_frecuentes.txt"
with open(output_file, "w", encoding="utf-8") as file:
    for word in sorted_words:
        #file.write(word + " " + str(word_counter[word]) + "\n")
        file.write(word + "\n")

print("Análisis de frecuencia completado. Palabras frecuentes guardadas en", output_file)

input("Presiona Enter para salir...")
