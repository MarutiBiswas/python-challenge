import os

import csv

csvpath = "Resources/election_data.csv"
total_votes = 0
candidates_name = []
candidates_vote = {}
percentage_vote = {}
populer_vote = {}

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
   
    for row in csvreader:
   
        total_votes = total_votes + 1
        name = row[2]
        if name not in candidates_name:
            candidates_name.append(name)
            candidates_vote[name] = 0
        candidates_vote[name] = candidates_vote[name] + 1

    for candidate in candidates_vote:
        vote = candidates_vote[candidate]
        per_vote = vote / total_votes
        percentage_vote[candidate] = per_vote
    print("Total votes",total_votes)
    print("candidates_name",candidates_name) 
    print("candidates_vote",candidates_vote)  
    print("percentage_vote",percentage_vote)