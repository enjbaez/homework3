## PyBank

import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        pybankcol = zip(row[1])
        print(pybankcol)
    