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


# Using the with statement open the file as a text file.
with open(file_to_load) as election_data:
    # Write some data to the file.
    #txt_file.write("Counties in the Election\n------------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)
    #Print each row is the csv file
    #for row in file_reader:
    #    print(row)

    #Read and print the header row
    headers = next(file_reader)
    print(headers)