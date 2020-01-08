## PyBank

import os
import CSV

# Path to collect data from the Resources folder
PyBank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# The total number of months included in the dataset
PyBank_csv.count

# The net total amount of "Profit/Losses" over the entire period
Profit/Losses.sum

# The average of the changes in "Profit/Losses" over the entire period
# row 2 minus row1 for each record then mean

# The greatest increase in profits (date and amount) over the entire period
# when row 2 is subtracted from row 1. the max of those results

# The greatest decrease in losses (date and amount) over the entire period
# when row 2 is subtracted from row 1. the min of those results

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
PyBank_csv.to_excel(r'C:\Users\ebaez\Desktop\homework3\PyBank\PyBank_Analyzed.xlsx')