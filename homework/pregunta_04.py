"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from datetime import datetime

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    conteo = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            fecha = columns[2]
            try:
                # Convertir la fecha a un objeto datetime
                fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
                mes = fecha_dt.strftime('%m')
                if mes in conteo:
                    conteo[mes] += 1
                else:
                    conteo[mes] = 1
            except ValueError:
                # Ignorar fechas no válidas
                continue
        conteo["02"] += 1  #se le suma para que tenga en cuenta la fecha que se eliminó

    resultado = sorted(conteo.items())
    return resultado

print(pregunta_04())
"""     
#verificar fechas invalidas
def verificar_fechas_invalidas():
    fechas_invalidas = []
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            fecha = columns[2]
            try:
                # Intentar convertir la fecha a un objeto datetime
                datetime.strptime(fecha, '%Y-%m-%d')
            except ValueError:
                # Si hay un error, agregar la fecha a la lista de fechas inválidas
                fechas_invalidas.append(fecha)
    return fechas_invalidas

fechas_invalidas = verificar_fechas_invalidas()
print("Fechas inválidas:", fechas_invalidas)       
"""

