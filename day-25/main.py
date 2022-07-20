

import csv 

with open("/Users/yuyuezhu/Documents/GitHub/python_bootcamp/day-25/weather_data.csv") as data_file:
    data = csv.reader(data_file)

    temperatures = []
    for row in data:
        try:
            temperatures.append(int(row[1]))
        except:
            pass

    print(temperatures)