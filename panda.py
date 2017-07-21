import pandas
import matplotlib.pyplot as pit

data = pandas.read_csv("weather_year.csv")

#print(data)

#print(len(data["Mean TemperatureF"]))

#print(data.columns)

#print(data["Max Temperature F"].head())

#print(data.EDT.head(10))

data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]

print(data.mean_temp.head(4))

data.max_temp.hist()
pit.show()

data.mean_dew.plot()
pit.show()

#print(freezing_days[freezing_days.min_temp >= 20])
#print(data.mean_temp.std())
