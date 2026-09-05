# process.py  
# grab some data, do a fake normalization, make a database

# imports
import csv
import sqlite3


# open a CSV file
    # load the data
def get_csv_data(filename):
    in_file = open(filename, 'r') # read only, don't want to change it
    temp_data = csv.reader(in_file)
    return temp_data


# separate a repeating qualifier out
    # we know our data, let's use sensor
def get_unique_values(csv_data):
    temp_data = []
    next(csv_data) # we know the first item is the header
    for row in csv_data:
        if row[2] in temp_data: # item 3 in the row is the sensor
            pass # skip if it exists, add if it doesn't
        else:
            temp_data.append(row[2])
    return temp_data

# create a new database file (not worried about servers right now)

# create a table to hold the repeating data
    # load the data

# create a table to hold referenced data 
# load the data


# main function to coordinate the action
if __name__ == "__main__":
    csv_data = get_csv_data("weather_data.csv")
    unique_fields = get_unique_values(csv_data)
    for row in unique_fields:
        print(row)
    
