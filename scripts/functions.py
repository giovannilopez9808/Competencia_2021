import pandas as pd
import datetime


def obtain_first_heat_data(data=pd.DataFrame(), first_heat=4):
    index = data.index[0:first_heat]
    data_heat = data[data.index.isin(index)]
    return data_heat


def obtain_heat_data(data=pd.DataFrame(), heat=5, first_heat=4):
    heat_down = (heat)*7+first_heat
    heat_up = (heat+1)*7+first_heat
    index = data.index[heat_down:heat_up]
    data_heat = data[data.index.isin(index)]
    return data_heat


def obtain_swimmers_per_test(data=pd.DataFrame(), test=""):
    data_test_1 = data[data["Prueba1"] == test]
    data_test_2 = data[data["Prueba2"] == test]
    data_test = pd.concat([data_test_1, data_test_2])
    return data_test


def obtain_swimmers_per_categorie(data=pd.DataFrame(), categorie=[]):
    data = data[data["Edad"] >= categorie[0]]
    data = data[data["Edad"] <= categorie[1]]
    return data


def obtain_total_heats(data=pd.DataFrame()):
    total_swimmers = len(data.index)
    heats = total_swimmers//7
    first_heat = total_swimmers-heats*7
    return first_heat, heats


def obtain_hour(hour=datetime.datetime(2000, 1, 1, 7, 30), minutes=5):
    hour = hour+datetime.timedelta(minutes=minutes)
    return hour


def write_schedule(LaTeX_tamplate, data_heat=pd.DataFrame(), time=datetime.datetime(2000, 1, 1, 1, 1), categorie="", test_data={}):
    if len(data_heat):
        time_str = time.strftime("%H:%M")
        schedule = LaTeX_tamplate.write_data(test=test_data["name"],
                                             time=time_str,
                                             categorie=categorie,
                                             data=data_heat)
        time = obtain_hour(time,
                           test_data["time"])
    return time
