import os

import csv

csvpath = "budget_data.csv"
total_months = 0
total_profit = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months = 1
    total_profit = int(first_row[1])
    p = int(first_row[1])

    gi = 0

    gd = 0
    for row in csvreader:
        print(row)
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        change = int(row[1]) - p
        if change > gi:
            gi = change
        p = int(row[1])



    print("Total months",total_months)
    print("Total profit",total_profit)
    print("Greatest Increase", gi)