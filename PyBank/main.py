# CSV data is loaded which contains two columns: Date and Profit/Losses
import csv
import os
csvpath =open('PyBank/Resources/budget_data.csv')

csvreader = csv.reader(csvpath, delimiter=',')
header_row = next(csvreader)
print(header_row)
# Firstly we create the list to store data:
profit = []
monthly_changes = []
date = []
# Then initialize the variables required -
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0
# The task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period
# To achieve this:
# Loop through data file to:
# 1. Count the number of months
# 2. Collect the greatest increase and decrease
# 3. Append the profit information and calculate the total profit
for row in csvreader:

                count = count + 1
                date.append(row[0])
                profit.append(row[1])
                total_profit = total_profit + int(row[1])
                final_profit = int(row[1])
                monthly_change_profits = final_profit - initial_profit
                monthly_changes.append(monthly_change_profits)
                total_change_profits = total_change_profits + monthly_change_profits
                initial_profit = final_profit
                average_change_profits = (total_change_profits/count)
                greatest_increase_profits = max(monthly_changes)
                greatest_decrease_profits = min(monthly_changes)
                increase_date = date[monthly_changes.index(greatest_increase_profits)]
                decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(int(average_change_profits)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
print("----------------------------------------------------------")

lines = ['Financial Analysis']
with open('financial_analysis.txt', 'w') as f:
        for line in lines:
                f.write(line)
                f.write('\n')
csvpath.close()