from functions import *
import pandas as pd
pd.options.mode.chained_assignment = None


class categories_list:
    def __init__(self):
        self.data = {"8": [0, 8],
                     "9-10": [9, 10],
                     "11-12": [11, 12],
                     "13-14": [13, 14],
                     "15-16": [15, 16],
                     "17-18": [17, 18]}


class test_list:
    def __init__(self):
        self.data = {"25D": {"name": "25 metros dorso",
                             "time": 2},
                     "25P": {"name": "25 metros pecho",
                             "time": 2},
                     "25M": {"name": "25 metros mariposa",
                             "time": 2},
                     "25L": {"name": "25 metros libre",
                             "time": 2},
                     "50D": {"name": "50 metros dorso",
                             "time": 2},
                     "50P": {"name": "50 metros pecho",
                             "time": 2},
                     "50L": {"name": "50 metros libre",
                             "time": 2},
                     "50M": {"name": "50 metros mariposa",
                             "time": 2},
                     "100L": {"name": "100 metros libre",
                              "time": 3},
                     "100P": {"name": "100 metros pecho",
                              "time": 3},
                     "100D": {"name": "100 metros dorso",
                              "time": 3},
                     "100CI": {"name": "100 metros combinado",
                               "time": 3}, }


class swimmers_data:
    def __init__(self, path="", file=""):
        self.path = path
        self.file = file
        self.read_data()
        self.sorted_by_ages()
        self.obtain_complete_name()

    def read_data(self):
        self.data = pd.read_csv("{}{}".format(self.path,
                                              self.file))

    def obtain_complete_name(self):
        self.data["Nombre completo"] = "A"
        for index in self.data.index:
            name = self.data["Nombre"][index].split(" ")[0]
            am = self.data["Apellido materno"][index]
            ap = self.data["Apellido paterno"][index]
            self.data["Nombre completo"][index] = "{} {} {}".format(ap,
                                                                    am,
                                                                    name)

    def sorted_by_ages(self):
        self.data = self.data.sort_values("Edad")


class schedule_template:
    def __init__(self, path="", test="", time="", categorie="", data=pd.DataFrame()):
        self.categorie = categorie
        self.swimmers = {}
        self.data = data
        self.path = path
        self.test = test
        self.time = time
        self.obtain_swimmers()
        self.sort_swimmers()
        self.write()

    def obtain_swimmers(self):
        lane = 4
        for i, index in enumerate(self.data.index):
            i = i+1
            self.input_swimmer(number=lane,
                               name=self.data["Nombre completo"][index],
                               team=self.data["Team"][index])
            if i % 2 == 1:
                i = i*-1
            lane += i

    def input_swimmer(self, number="", name="", team=""):
        swimmer = {number: {"name": name,
                            "team": team, }}
        self.swimmers.update(swimmer)

    def sort_swimmers(self):
        sorted_swimmers = {}
        for lane in range(1, 8):
            try:
                swimmer = self.swimmers[lane]
                swimmer = {lane: swimmer}
                sorted_swimmers.update(swimmer)
            except:
                pass
        self.swimmers = sorted_swimmers

    def write(self):
        file = open("{}schedule.tex".format(self.path),
                    "a")
        file.write("\\begin{minipage}{0.95\linewidth}\\vspace{0.5cm} \n")
        file.write("\\begin{flushleft}\n")
        file.write("\\textbf{\n")
        file.write("\hspace{-0.15cm}")
        file.write("{}".format(self.test))
        file.write("\hspace{1.5cm}")
        file.write("{} hrs \\\\".format(self.time))
        file.write("Categoria {} años".format(self.categorie))
        file.write("}\\vspace{-0.2cm} \n")
        file.write("\end{flushleft}\n")
        file.write("\\begin{tabular}{cp{0.63\linewidth}l}\n")
        file.write("\hline\n")
        file.write("& \\textbf{Nombre} & \\textbf{Equipo} \\\\ \hline\n")
        for index in self.swimmers:
            file.write("{} & {} & {} \\\\ \n".format(index,
                                                     self.swimmers[index]["name"],
                                                     self.swimmers[index]["team"]))
        file.write("\end{tabular}\n")
        file.write("\end{minipage}\n")
        file.close()
