import os
import csv

csv_path = os.path.join("Election_Data.csv")

candidate = []
votes = []
rows = 0
winner = 0
winner_name = ""
i = 0

with open(csv_path, newline = "") as csvfile:
	csv_reader = csv.reader(csvfile, delimiter = ",")
	next(csv_reader, None)
	for row in csv_reader:
		rows = rows + 1
		if row[2] not in candidate:
			candidate.append(row[2])
			votes.append(0)
		else:
			votes[candidate.index(row[2])] = votes[candidate.index(row[2])] + 1

winner = max(range(len(votes)), key = lambda x: votes[x])
winner_name = candidate[int(winner)]

print("Election Results:")
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
print("Total Votes: " + str(rows))
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
while i <= (len(candidate) - 1):
	print(candidate[i] + ": " + str(round((votes[i]/rows * 100),2)) + "% (" + str(votes[i]) + ")")
	i = i + 1
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
print("Winner: " + str(winner_name))
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")


i = 0
save_file = csv_path.strip(".csv") + " Analysis.txt"
filepath = os.path.join(".", save_file)
with open(filepath, "w") as text:
	text.write("Election Results:\n")
	text.write("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")
	text.write("Total Votes: " + str(rows) + "\n")
	text.write("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")
	while i <= (len(candidate) - 1):
		text.write(candidate[i] + ": " + str(round((votes[i]/rows * 100),2)) + "% (" + str(votes[i]) + ")\n")
		i = i + 1
	text.write("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")
	text.write("Winner: " + str(winner_name) + "\n")
	text.write("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")