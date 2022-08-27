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

# Create the output file
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Skip the first row (header)
    headers = next(file_reader)
    print(headers)

 #   for row in file_reader:
 #       print(row)
