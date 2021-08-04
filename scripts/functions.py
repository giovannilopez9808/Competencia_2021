import pandas as pd
import datetime


def obtain_first_heat_data(data=pd.DataFrame(), first_heat=4):
    """
    Obtiene la información de los nadadores que nadaran en el primer heat de cada prueba y categoria

    Inputs:
    + first_time -> numero de nadadores que iran en el primer heat
    + data -> data de los nadadores de esa prueba
    """
    index = data.index[0:first_heat]
    data_heat = data[data.index.isin(index)]
    return data_heat


def obtain_heat_data(data=pd.DataFrame(), heat=5, first_heat=4):
    """
    Obtiene la información de los nadadores que nadaran en el heat número `heat`

    Inputs:
    + first_time -> numero de nadadores que iran en el primer heat
    + data -> data de los nadadores de esa prueba
    + heat -> numero de heat a nadar
    """
    heat_down = (heat)*7+first_heat
    heat_up = (heat+1)*7+first_heat
    index = data.index[heat_down:heat_up]
    data_heat = data[data.index.isin(index)]
    return data_heat


def obtain_swimmers_per_test(data=pd.DataFrame(), test=""):
    """
    Obtiene los nadadores que nadaran una prueba

    Inputs:
    + data -> data de todos los nadadores
    + test -> código de prueba a nadar
    """
    data_test_1 = data[data["Prueba1"] == test]
    data_test_2 = data[data["Prueba2"] == test]
    data_test = pd.concat([data_test_1, data_test_2])
    return data_test


def obtain_swimmers_per_categorie(data=pd.DataFrame(), categorie=[]):
    """
    Obtiene los nadadores de cada categoria

    Inputs:
    + categorie -> lista con los limites de edad de cada categoria
    + data -> data de los nadadores de esa prueba
    """
    data = data[data["Edad"] >= categorie[0]]
    data = data[data["Edad"] <= categorie[1]]
    return data


def obtain_total_heats(data=pd.DataFrame()):
    """
    Obtiene el total de heats de cada prueba

    Inputs:
    + data -> data de los nadadores de esa prueba
    """
    total_swimmers = len(data.index)
    heats = total_swimmers//7
    first_heat = total_swimmers-heats*7
    return first_heat, heats


def obtain_hour(hour=datetime.datetime(2000, 1, 1, 7, 30), minutes=5):
    """
    Suma unos mínutos dados a la hora ingresada

    Inputs:
    + minutes -> minutos a sumar a la hora
    + hour -> hora inicial
    """
    hour = hour+datetime.timedelta(minutes=minutes)
    return hour


def write_schedule(LaTeX_tamplate, data_heat=pd.DataFrame(), time=datetime.datetime(2000, 1, 1, 1, 1), categorie="", test_data={}):
    """
    Escribe el heat en el formato LaTeX para el itenerario

    Inputs:
    + LaTeX_template -> Clase que contiene la logistica para escribir el archivo de LaTeX
    + data_head -> información de nadadores del heat
    + test_cata -> información de la prueba a nadar
    + time -> hora a la cual se nadara el heat
    + categorie -> categoria de los nadadores 
    """
    if len(data_heat):
        time_str = time.strftime("%H:%M")
        schedule = LaTeX_tamplate.write_data(test=test_data["name"],
                                             time=time_str,
                                             categorie=categorie,
                                             data=data_heat)
        time = obtain_hour(time,
                           test_data["time"])
    return time
