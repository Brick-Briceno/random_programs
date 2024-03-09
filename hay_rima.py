texto = ""
try:
    texto += open("palabras.txt", encoding="utf-8").read() + "\n"
except UnicodeDecodeError:
    texto += open("palabras.txt", encoding="ansi").read() + "\n"


def riman(palabra1, palabra2):
    vocales = "aeiou" + "áéíúó"    
    if palabra1[-1:] == "y":
        palabra1 = palabra1[:-1] + "i"
    if palabra2[-1:] == "y":
        palabra2 = palabra2[:-1] + "i"

    vocales = tuple(vocales + vocales.upper())
    ultimas_vocales1 = [letra for letra in reversed(palabra1) if letra.lower() in vocales][:2]
    ultimas_vocales2 = [letra for letra in reversed(palabra2) if letra.lower() in vocales][:2]

    return ultimas_vocales1 == ultimas_vocales2

print("Cargando de palabras...")
palabras = texto.split()
print("Palabras cargadas\n")


while True:
    palabra = input("Introduce una palabra> ")
    for x in range(len(palabras)):
        if riman(palabras[x], palabra):
            print(palabras[x])

    print("\nlisto! :D\n")
