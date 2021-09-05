import pandas

import seaborn

import matplotlib.pyplot as mp

# loading the .txt file as the dataset
data = pandas.read_csv("C:/Users/aditya gaur/OneDrive/Desktop/DataScience/UberDataAnalysis/uber-raw-data-apr14.txt")

# used to check the dataset and the values it contains
print(data)

print(data.head())  # used to print the first 5 values

print(data.tail())  # used to print the last 5 values

# Converting Date and Time string to numerical values

data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)  # .to_datetime converts the time string to a timestamp


# Function to find the date of the month for ride

def get_date(dt):
    return dt.day

# Adding a Date of Month column to the data set for better data understanding

data['DOM'] = data['Date/Time'].map(get_date)  # 'DOM' is Date of the Month

print(data.head())


# Function to get the day of week for ride

def get_weekday(dt):
    return dt.weekday()

# Adding a Day of Week column to the data set for better data understanding

data["Weekday"] = data['Date/Time'].map(get_weekday)


# Function to get the hour of the day at which booking was done

def get_hour(dt):
    return dt.hour

# Adding a Ride Hour column to the data set for better data understanding

data["Hour"] = data['Date/Time'].map(get_hour)

print(data)


# analyzing the Date of the month

mp.hist(data.DOM, bins=30, rwidth=0.8, range=(0.5, 30.5))

mp.xlabel("date of the month")

mp.ylabel("Frequency")

mp.title("Frequency by DoM")

mp.show()


def count_rows(rows):
    return len(rows)


by_date = data.groupby("DOM").apply(count_rows)
print(by_date)

mp.bar(range(1, 31), by_date)

mp.ylabel("Frequency")

mp.xlabel("Date of Months")

mp.show()

by_date_sorted = by_date.sort_values()
print(by_date_sorted)

mp.figure(figsize=(20, 3))
mp.bar(range(1, 31), by_date_sorted)
mp.xticks(range(1, 31), by_date_sorted.index)
mp.xlabel("Date of month")
mp.ylabel("Frequency")
mp.title("Frequency by DoM (Uber April 2014)")

mp.show()

# Analyzing the Hour

mp.hist(data.Hour, bins=24, range=(0.5, 24))
mp.show()

mp.hist(data.Weekday, bins=7, range =(-.5,6.5), rwidth=.8, color='#AA6666', alpha=.4)
mp.xticks(range(7), 'Mon Tue Wed Thu Fri Sat Sun'.split())
mp.show()

# Cross analysis(hour, Day of Week)

by_cross = data.groupby('Weekday Hour'.split()).apply(count_rows).unstack()
seaborn.heatmap(by_cross)
mp.show()

mp.hist(data['Lat'], bins=100, range=(40.5, 41))
mp.ylabel("Frequncy")
mp.xlabel("Latitudes")
mp.show()

mp.hist(data['Lon'], bins=100, range=(-74.1, -73.9))
mp.ylabel("Frequncy")
mp.xlabel("Longitudes")
mp.show()

mp.hist(data['Lon'], bins=100, range=(-74.1, -73.9), color='g', alpha=.5, label='longitude')
mp.grid()
mp.legend(loc='upper left')
mp.twiny()
mp.hist(data['Lat'], bins=100, range=(40.5, 41), color='r', alpha=.5, label='latitude')
mp.legend(loc='best')
mp.show()

mp.figure(figsize=(20, 20))
mp.plot(data['Lon'], data['Lat'], '.', ms=1, alpha=.5)
mp.xlim(-74.2, -73.7)
mp.ylim(40.7, 41)
mp.show()
