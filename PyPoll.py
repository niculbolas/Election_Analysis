##################################################################################################
#Program outline:
#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3 The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
##################################################################################################
# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Declare vote counting variable
total_votes = 0

#Declare candidate options list
candidate_options = []

#Declare dictionary for counting candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    for row in file_reader:
        
        #Increment vote counter
        total_votes += 1
        
        #Get candidate name
        candidate_name = row[2]
        
        #Add candidate to options list if they are not already
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #Start tracking that candidates votes
            candidate_votes[candidate_name] = 0

        #Increment candidate's vote counter
        candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping through the counts.
#Iterate through the candidate list.
for candidate_name in candidate_votes:
    
    #Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    
    #Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    #Determine winning vote count and candidate
    #Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        
        #If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        
        #Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

    #Print results for each candidate
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#Printer winner
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)