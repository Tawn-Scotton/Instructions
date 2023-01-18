import csv
import os
from collections import Counter

# global variable to get the current directory path 
curr_path = os.path.dirname(__file__) 

# global variable - use the current path to get Resources folder and the file we want to open
csv_file = curr_path + "\\Resources\\election_data.csv"

# this function finds the total number of votes for the csv file
def total_number_votes():
    # this variable will hold the line numbers
    total_vote_count = 0
    # opening the CSV file - using with open since it automatically closes the file when done
    with open(csv_file, mode ='r') as file:
        # reading the CSV file
        csv_reader = csv.reader(file) 
        # convert to list for easy counter
        csv_list = list(csv_reader)
        # count the rows of the CSV file wile open
        for i in range(len(csv_list)): 
            total_vote_count = i
    return total_vote_count

# this function finds the candidates that received votes - returns a dictionary with nanes and number of votes each
def candidates_receiving_votes():
    # this holds the candidates list with duplicates   
    candidate_list_with_dupes = []
    # this holds a dictionary of candidate names and votes
    candidate_names_votes_dict = []
    # opening the CSV file - using with open since it automatically closes the file when done
    with open(csv_file, mode ='r') as file:
        # reading the CSV file using dictionary reader
        csv_dict_reader = csv.DictReader(file)  
         # loop through the dictionary reader and place candidates in a list
        for row in csv_dict_reader:
            candidate_list_with_dupes.append(row["Candidate"])

    candidate_names_votes_dict  = Counter(candidate_list_with_dupes)      
    return candidate_names_votes_dict

# this function displays and writes to file the election results
def display_election_results():
    # get the total number of votes
    total_vote_count = total_number_votes()
    # get a dictionary with candidates names, percentage of votes, and vote total
    candidate_names_votes_dict = candidates_receiving_votes()
    percentage_of_votes = ""
    highest_votes = 0
    winner = ""
    candidate_data = ""
    # Get the percentage of votes and winner
    for candidate, number_votes in candidate_names_votes_dict.items():
        percentage_of_votes = str(round(number_votes / total_vote_count * 100, 3)) + "%"
        if number_votes > highest_votes:
            highest_votes = number_votes
            winner = candidate
        candidate_data += candidate + ": " + percentage_of_votes + " (" + str(number_votes) + ")\n"

    election_result = ( "Election Results\n" +
                        "-------------------------\n" +
                        "Total Votes: " + str(total_number_votes()) + "\n" +
                        "-------------------------\n" +
                        candidate_data +
                        "Winner: " + winner)                        
    
    print(election_result)
    with open(curr_path + "\\analysis\\election_results.txt", mode ='w') as file:
        file.write(election_result)

# Call main function to display and write to file election results
display_election_results()