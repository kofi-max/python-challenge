
# Objective 1: Import modules os and csv. Importing numpy in order to use the unique function
import os
import csv

# Objective 2: Set the path for the CSV file in PyPollcsv


# Objective 3: Create the lists to store data. Initialize

# Open the CSV using the set path PyPollcsv
csvpath =open('PyPoll/Resouces/election_data.csv')

csvreader = csv.reader(csvpath, delimiter=',')
header_row = next(csvreader)
print(header_row)
print('..................')
count = 0
candidatelist = []
unique_candidate = []
number_votes_count = []
percent_votes = []
total_votes = 0
for row in csvreader:
        # Add to our vote-counter 
        total_votes += 1
        if row[2] not in unique_candidate:
            unique_candidate.append(row[2])
            index = unique_candidate.index(row[2])
            number_votes_count.append(1)
        else:
            index = unique_candidate.index(row[2])
            number_votes_count[index] += 1
for votes in number_votes_count:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
winner = max(number_votes_count)
index = number_votes_count.index(winner)
winning_candidate = unique_candidate[index]
# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(unique_candidate)):
    print(f"{unique_candidate[i]}: {str(percent_votes[i])} ({str(number_votes_count[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")
lines = ['Election Results']
with open('Election Results.txt', 'w') as f:
        for line in lines:
                f.write(line)
                f.write('\n')
csvpath.close()    
