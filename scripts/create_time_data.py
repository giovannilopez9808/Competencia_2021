from Class_list import *


def clean_data(data=pd.DataFrame()):
    columns = data.columns
    columns = columns.drop("Nombre completo")
    data = data.drop(columns, 1)
    return data


parameters = {"path data": "../data/",
              "file data": "dummy_data.csv",
              "file time": "time_data.csv"}
swimmers = swimmers_data(parameters["path data"],
                         parameters["file data"])
swimmers.data = clean_data(swimmers.data)
test = test_list()
tests = test.data.keys()
time_data = pd.DataFrame(index=swimmers.data["Nombre completo"],
                         columns=tests)
time_data.to_csv("{}{}".format(parameters["path data"],
                               parameters["file time"]))
