import base64

#Cifrar
texto_original = "Oh dios! que rico follas, si sii! dale, me encantaria que lo hicieramos todas las noches! ohh"

# Codificar en Base64
texto_cifrado = base64.b64encode(texto_original.encode("utf-8")).decode("utf-8")



print(texto_cifrado)

#Descifrar

texto_cifrado = "SG9sYSwgdGVzdG8gZWwgZW4gdGV4dG8gcGFyYSBjaWZyYXIgZW4gQmFzZTY0Lg=="

# Decodificar desde Base64
texto_descifrado = base64.b64decode(texto_cifrado).decode("utf-8")

print(texto_descifrado)
