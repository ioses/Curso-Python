import csv

with open("Files/weather.csv") as file:
    data = list(csv.reader(file))