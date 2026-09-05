# process.py  
# grab some data, do a fake normalization, make a database

# imports
import csv

# open a CSV file
    # load the data
def get_csv_data(filename):
    in_file = open(filename, 'r')
    tmp_data = csv.reader(in_file)
    return tmp_data

# separate a repeating qualifier out
    # we know our data, let's use sensor

# create a new database file (not worried about servers right now)

# create a table to hold the repeating data
# load the data

# create a table to hold referenced data 
# load the data


# main function to coordinate the action
if __name__ == "__main__":
    print("starting process")
    csv_data = get_csv_data("weather_data.csv")
    for row in csv_data:
        print(row)
        
    
