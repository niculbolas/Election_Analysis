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

#Declare county options list
county_options = []

#Declare dictionary for counting candidate votes
candidate_votes = {}

#Declare dictionary for counting county votes
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Biggest county turnout and count tracker
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

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

        #Get county name
        county_name = row[1]
        
        #Add candidate to options list if they are not already
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #Start tracking that candidates votes
            candidate_votes[candidate_name] = 0

        #Increment candidate's vote counter
        candidate_votes[candidate_name] += 1

        #Add county to options list if it is not already
        if county_name not in county_options:
            county_options.append(county_name)

            #Start tracking that counties votes
            county_votes[county_name] = 0
        
        #Increment county vote counter
        county_votes[county_name] += 1

    #Save the results to our text file.
    with open(file_to_save, "w") as txt_file:

        #Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
            f"\n")
        print(election_results, end="")
                
        #Save the final vote count to the text file.
        txt_file.write(election_results)

        #Start the county votes section
        print(f"County Votes:\n")
        txt_file.write(f"County Votes:\n")
        
        #Determine the percentage of votes for each county by looping through the countys.
        #Iterate through the county list
        for county_name in county_votes:
            votes = county_votes[county_name]
            vote_percentage = float(votes) / float(total_votes) * 100

            #Print each county, the vote county, and percentage to the terminal
            county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(county_results)

            #Save the candidate results to the text file
            txt_file.write(county_results)

            #Determine winning county vote count and percentage
            if(votes > winning_county_count) and (vote_percentage > winning_county_percentage):
                winning_county_count = votes
                winning_county = county_name
                winning_county_percentage = vote_percentage

        #Print the winning county's results to the terminal
        winning_county_summary = (
            f"\n"
            f"-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n")
        print(winning_county_summary)

        # Save the winning county's name to the text file.
        txt_file.write(winning_county_summary)
        
        #Determine the percentage of votes for each candidate by looping through the counts.
        #Iterate through the candidate list.
        for candidate_name in candidate_votes:
        
            # Retrieve vote count and percentage.
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            
            # Print each candidate, their voter count, and percentage to the terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)

            #Save the candidate results to the text file
            txt_file.write(candidate_results)

            # Determine winning vote count, winning percentage, and candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage
        
        #Print the winning candidate's results to the terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)
