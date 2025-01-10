"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    conteo = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            key = columns[0]
            valores = [int(v.split(':')[1]) for v in columns[4].split(',')]
            value = sum(valores)
            if key not in conteo:
                conteo[key] = value
            else:
                conteo[key] += value
    return conteo

