import os
import csv

csv_path = os.path.join("budget_data.csv")

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")



    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)
