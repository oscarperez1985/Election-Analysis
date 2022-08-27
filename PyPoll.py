#================================================================================
# Challenge of Module 3: Election Analysis
#================================================================================
##________________________________________________________________________________
# Objective:
# The script should be able to deliver the following information:
# The file to open
#   1. The total number of votes cast
#   2. A complete list of candidates who received votes
#   3. The percentage of votes each candidate won
#   4. The total number of votes each candidate won
#   5. The winner of the election based on popular vote 
#________________________________________________________________________________

# Import Modules
import os
import csv

# Declare input and output file path/names
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize the total vote counter
total_votes = 0

# Candidate options list
candidate_options = []

# Create a dictionary of candidate: votes
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Create the output file
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Skip the first row (header)
    headers = next(file_reader)

    # Print each row in the input file
    for row in file_reader:
        #print(row)
        
        # Update the vote count
        total_votes += 1

        # Print the candidate name for each row
        candidate_name = row[2]

        # Add the candidate name if not in the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            # Initialize that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
# note: i is candidate names in the original code
for i in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[i]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out each candidate's name, vote count, and percentage of votes to the terminal
    # votes to the terminal

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true, then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # And set the winning candidate equal to the candidate's name
        winning_candidate = i

    # To do, print out the winning candidate, vote count and percentage to the terminal
    print(f"{i}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

    # 4. Print the candidate name and percentage of votes.
    #print(f"{i}: received {vote_percentage:.1f}% of the vote.")

# 3. Print outputs
#print(total_votes)
#print(candidate_options)
#print(candidate_votes)
