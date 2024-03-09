import requests

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  #Verificar si la solicitud fue exitosa
        html_content = response.text
        return html_content
    except requests.exceptions.RequestException as e:
        print("Error al acceder a la URL:", e)

def txt_a_archivo(texto):
    with open("html_paginas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(texto + "\n")

while True:
    url = input("Url> ")
    if url == "salir":
        break
    try:
        txt_a_archivo(get_html(url))
        print("Html Guaardado!!! :D")
    except:
        None
