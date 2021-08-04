from Class_list import *
from functions import *

parameters = {"path data": "../data/",
              "path schedule": "../template/Files/",
              "file data": "dummy_data.csv",
              "hour initial": 9}

time = datetime.datetime(2020, 9, 1, 9, 0)
swimmers = swimmers_data(parameters["path data"],
                         parameters["file data"])
tests = test_list()
LaTeX_template = schedule_template(parameters["path schedule"])
categories = categories_list()
for test in tests.data:
    data_per_test = obtain_swimmers_per_test(swimmers.data,
                                             test)
    for categorie in categories.data:
        data = obtain_swimmers_per_categorie(data_per_test,
                                             categories.data[categorie])
        test_data = tests.data[test]
        first_heat, heats = obtain_total_heats(data)
        data_heat = obtain_first_heat_data(data,
                                           first_heat)
        time = write_schedule(LaTeX_template,
                              data_heat,
                              time,
                              categorie,
                              test_data)
        for heat in range(heats):
            data_heat = obtain_heat_data(data,
                                         heat,
                                         first_heat)
            time = write_schedule(LaTeX_template,
                                  data_heat,
                                  time,
                                  categorie,
                                  test_data)
