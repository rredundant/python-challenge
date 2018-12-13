import os
import csv
unique_votes = 0
candidate_votes = {}


with open('election_data.csv', 'r') as f:
    reader = csv.reader(f,)
    next(reader)
    for row in reader:
        unique_votes += 1
        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 1
        elif row[2] in candidate_votes:
            candidate_votes[row[2]] += 1
            
            
percent_votes = {candidate: vote / unique_votes for candidate, vote in candidate_votes.items()}


winner = ""
winning = 0
for candidate, percent in percent_votes.items():
    if percent > winning:
        winning = percent
        winner = candidate
        
print("Election Results")
print(f"Total Votes: {unique_votes}")
for candidate, percent in percent_votes.items():
    print(f"{candidate}:  {round(percent * 100, 2)}%")
print(f"Winner: {winner}")

file = open("Election_Results.txt", "w")
file.write("Election Results" + "\n")
file.write(f"Total Votes: {unique_votes}" + "\n")
for candidate, percent in percent_votes.items():
    file.write(f"{candidate}:  {round(percent * 100, 2)}%" + "\n")
file.write(f"Winner: {winner}")
file.close()