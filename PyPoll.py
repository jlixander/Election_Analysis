#1 Open the data File
#2 Write down the names of all the candidates
#3 Add a vote count for each candidate
#4 Get the total votes for each candidate
#5 Get the total votes cast for the election
 
import csv
import os

#Load csv file to var file_to_load
#file_to_load = 'Resources\election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")


#Open to read the data in var file_to_load and read it.
#election_data = open(file_to_load,'r')
#To-do analysis
#close the file.
#election_data.close()

#Open file w with function
#with open(file_to_load) as election_data:
   #To-analysis
#   print(election_data)

# Create a variable to save file to path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
    #Write data to file.
#   outfile.write("Hello World")
#Close the file
#outfile.close()

#Initialize total vote counter
total_votes = 0
#Create a list that holds all candidate names
candidate_options = []
#Create a dictionary for keeping count of votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Using the with statement open the file as a text file.
with open(file_to_load) as election_data:
    # Write some data to the file.
    #txt_file.write("Counties in the Election\n------------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)


    #Read and print the header row
    headers = next(file_reader)
    #print(headers)

    #Print each row is the csv file
    for row in file_reader:
        total_votes +=1
        #Print the candidate name from each row
        candidate_name = row[2]
        #Comb through list of candidates and add if not found in options
        if candidate_name not in candidate_options:
            #Insert new candidate name if not found in list candidate_options
            candidate_options.append(candidate_name)
            #Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's vote count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

#print(total_votes)
#print(candidate_votes)