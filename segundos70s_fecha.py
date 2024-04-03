import datetime

def segundos70s_fecha(s):
    #Arroja año, mes, dia, hora, minutos, segundos
    fecha_hora = datetime.datetime.fromtimestamp(s)
    fecha_final = []
    for x in fecha_hora.strftime("%Y-%m-%d %H%M%S").replace("-",  ).replace(":", "").split():
        fecha_final.append(int(x))
    return fecha_final
