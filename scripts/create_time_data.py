from Class_list import *


def clean_data(data=pd.DataFrame()):
    columns = data.columns
    columns = columns.drop(["Nombre completo", "Edad"])
    data = data.drop(columns, 1)
    return data


parameters = {"path data": "../data/",
              "file data": "data.csv",
              "file time": "time_data.csv"}
test = test_list()
tests = test.data.keys()
swimmers = swimmers_data(parameters["path data"],
                         parameters["file data"])
swimmers.data = clean_data(swimmers.data)
time_data = swimmers.data
time_data[list(tests)] = ""
time_data.to_csv("{}{}".format(parameters["path data"],
                               parameters["file time"]),
                 index=False)
