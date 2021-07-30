from Class_list import *
import datetime


def obtain_swimmers_per_test(data=pd.DataFrame(), test=""):
    data_test_1 = data[data["Prueba1"] == test]
    data_test_2 = data[data["Prueba2"] == test]
    data_test = pd.concat([data_test_1, data_test_2])
    return data_test


def obtain_total_heats(data=pd.DataFrame()):
    total_swimmers = len(data.index)
    heats = total_swimmers//7
    first_heat = total_swimmers-heats*7
    return first_heat, heats


def obtain_hour(hour, minutes):
    hour = hour+datetime.timedelta(minutes=minutes)
    return hour


parameters = {"path data": "../data/",
              "path schedule": "../schedule/Files/",
              "file data": "dummy_data.csv",
              "hour initial": 9}
time = datetime.datetime(2020, 9, 1, 9, 0)
swimmers = swimmers_data(parameters["path data"],
                         parameters["file data"])
tests = test_list()
for test in tests.tests_data:
    data = obtain_swimmers_per_test(swimmers.data,
                                    test)
    test_data = tests.tests_data[test]
    first_heat, heats = obtain_total_heats(data)
    index = data.index[0:first_heat]
    data_heat = data[data.index.isin(index)]
    if len(data_heat):
        time_str = time.strftime("%H:%M")
        schedule = schedule_template(path=parameters["path schedule"],
                                     test=test_data["name"],
                                     time=time_str,
                                     data=data_heat)
        time = obtain_hour(time,
                           test_data["time"])
    for heat in range(heats):
        heat_down = (heat)*7+first_heat
        heat_up = (heat+1)*7+first_heat
        index = data.index[heat_down:heat_up]
        data_heat = data[data.index.isin(index)]
        if len(data_heat):
            time_str = time.strftime("%H:%M")
            schedule = schedule_template(path=parameters["path schedule"],
                                         test=test_data["name"],
                                         time=time_str,
                                         data=data_heat)
            time = obtain_hour(time,
                               test_data["time"])
