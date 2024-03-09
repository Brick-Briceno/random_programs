from pytube import YouTube, Playlist
import re

def descargar_video(url, ruta, resolucion):
    """
    Descarga un video de YouTube en una resolución específica.

    Parámetros:
    - url (str): URL del video de YouTube.
    - ruta (str): Ruta completa donde se guardará el video.
    - resolucion (str): Resolución deseada (por defecto: "max")"""

    video = YouTube(url)

    # Filtra las corrientes por resolución
    if resolucion.lower() == "max":
        chosen_stream = video.streams.get_highest_resolution()
    else:
        filtered_streams = video.streams.filter(res=resolucion, file_extension="mp4")
        chosen_stream = filtered_streams.first()

    # Descarga el video en la ubicación especificada
    chosen_stream.download(output_path=ruta)

def es_url_lista_reproduccion(url):
    try:
        playlist = Playlist(url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        return playlist, playlist.title
    except: return


#Ejemplo de uso:

#tamano_archivo = chosen_stream.filesize
#bytes_descargados = chosen_stream.downloaded_bytes


#descargar_video("https://www.youtube.com/watch?v=FNt8UnD2Jl4", "", "max")
print(es_url_lista_reproduccion("https://www.youtube.com/watch?v=60ItHLz5WEA&list=PLw-VjHDlEOgs658kAHR_LAaILBXb-s6Q5"))
