# process2.py
# grab some data, do a fake normalization, make a database

# imports
import csv
import sys
import sqlite3


# open a CSV file
    # load the data
def get_csv_data(filename):
    # the with block closes the file for us when we're done reading
    with open(filename, 'r', newline='') as in_file:
        temp_data = csv.reader(in_file)
        header = next(temp_data)  # we know the first item is the header
        rows = list(temp_data)    # a reader can only be read once, so keep the rows in a list
    return header, rows


# separate a repeating qualifier out
    # we know our data, let's use sensor
def get_unique_values(rows):
    temp_data = []
    for row in rows:
        if row[2] in temp_data:  # item 3 in the row is the sensor
            pass  # skip if it exists, add if it doesn't
        else:
            temp_data.append(row[2])
    return temp_data


# create a new database file (not worried about servers right now)
def get_database(filename):
    database = sqlite3.connect(filename)
    database.execute('PRAGMA foreign_keys = ON')  # SQLite only enforces foreign keys if asked
    return database


# create a table to hold the repeating data
    # load the data
def load_repeating_data(database, data):
    cur = database.cursor()
    # readings points at sensors, so drop it first
    cur.execute('''DROP TABLE IF EXISTS readings''')
    cur.execute('''DROP TABLE IF EXISTS sensors''')
    cur.execute('''CREATE TABLE "sensors" ("sensor" TEXT UNIQUE, "sensorId" INTEGER NOT NULL UNIQUE, PRIMARY KEY("sensorId" AUTOINCREMENT))''')
    database.commit()
    for row in data:
        cur.execute('''INSERT INTO sensors (sensor) VALUES (?)''', [row,])
    database.commit()
    cur.close()
    return


# get the data we just loaded into the reference table
    # then we can replace the sensors with ids
def get_loaded_data(database):
    cur = database.cursor()
    res = cur.execute('''SELECT sensor, sensorId FROM sensors''')
    lookup = dict(res.fetchall())  # {'Garage': 1, 'Kitchen': 2, ...}
    cur.close()
    return lookup


# create a table to hold referenced data
    # load the data
def load_referenced_data(database, rows, lookup):
    cur = database.cursor()
    cur.execute('''CREATE TABLE "readings" (
                       "reading_id"   INTEGER PRIMARY KEY,
                       "reading_date" TEXT,
                       "sensorId"     INTEGER NOT NULL,
                       "temperature"  REAL,
                       "humidity"     REAL,
                       "pressure"     REAL,
                       FOREIGN KEY("sensorId") REFERENCES sensors("sensorId"))''')
    database.commit()
    for row in rows:
        reading_id, date, sensor, temp, humid, press = row
        cur.execute('''INSERT INTO readings VALUES (?, ?, ?, ?, ?, ?)''',
                    [int(reading_id),
                     date,
                     lookup[sensor],  # the actual swap: name in, id out
                     float(temp),
                     float(humid),
                     float(press) or None])  # a pressure of 0 means "no reading", store it as NULL
    database.commit()
    cur.close()
    return


# check our work
def check_results(database):
    cur = database.cursor()
    count = cur.execute('''SELECT COUNT(*) FROM readings''').fetchone()
    print('readings loaded:', count[0])
    res = cur.execute('''SELECT s.sensor, COUNT(*), ROUND(AVG(r.temperature), 1)
                         FROM readings r
                         JOIN sensors s ON s.sensorId = r.sensorId
                         GROUP BY s.sensor''')
    for row in res.fetchall():
        print(row)
    cur.close()


# main function to coordinate the action
if __name__ == "__main__":
    # if we don't specify an input file, use a standard one
    if len(sys.argv) < 2:
        filename="weather_data_100k.csv"
    else:
        filename = sys.argv[1]
        
    header, rows = get_csv_data(filename)
    unique_fields = get_unique_values(rows)
    my_database = get_database("weather.db")
    load_repeating_data(my_database, unique_fields)
    lookup = get_loaded_data(my_database)
    load_referenced_data(my_database, rows, lookup)
    check_results(my_database)
    my_database.close()
