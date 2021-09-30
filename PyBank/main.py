# CSV data is loaded which contains two columns: Date and Profit/Losses
import csv
import os
csvpath = os.path.join('C:\Users\User\Desktop\ubhm-brm-data-pt-06-2021-u-c\Homeworks\03-Python\Instructions\PyBank\Resources\budget_data.cvs')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header_row = next(csvreader)
    print(header_row)

