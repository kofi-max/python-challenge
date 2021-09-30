# CSV data is loaded which contains two columns: Date and Profit/Losses
import csv
import os
csvpath = os.path.join('/Resources/budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header_row = next(csvreader)
    print(header_row)

