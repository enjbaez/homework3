import os
import CSV

# Path to collect data from the Resources folder
Pypoll_csv = os.path.join('..', 'Resources', 'election_data.csv')

# The total number of votes cast
Pypoll_csv.count

# A complete list of candidates who received votes
Pypoll_csv = list(set(Pypoll_csv))

# The percentage of votes each candidate won
Pypoll_csv_percentage = (votes per candidate / total_votes) * 100)

# The total number of votes each candidate won
candidate.count("voter id")

# The winner of the election based on popular vote.
print.candidate(Pypoll_csv_percentage)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
Pypoll_csv.to_excel(r'Path where you want to store the exported excel file\File Name.xlsx')



