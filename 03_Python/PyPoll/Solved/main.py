import os
import csv

#set the path for file
election_csv = "../Resources/election_data.csv"


#Initialize variable
candidates, total_candidates, candidate_perc, candidate_total, summaries = ([] for i in range(5))

#Open the CSVFile
    
with open(election_csv, mode='r', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	next(csvreader)

	num_rows = 0

#loop through all the rows in csvfile
	for row in csvreader:
		total_candidates.append(row[2])
		num_rows += 1
    	

#sorted list the total candicates 
sorted_candidates = sorted(total_candidates)

# loop through the row


for i in range(num_rows):
    if sorted_candidates[i - 1] != sorted_candidates[i]:
        candidates.append(sorted_candidates[i])

#   Output Summary

print("\ntext")
print("\nElection Results")
print("---------------------------")
print("Total Votes:", num_rows)
print("---------------------------")

#for loop
for j in range(len(candidates)):
    candidate_count = 0
    for k in range(len(sorted_candidates)):
        if candidates[j] == sorted_candidates[k]:
            candidate_count += 1
    candidate_perc.append(round(candidate_count / num_rows * 100, 3))
    candidate_total.append(candidate_count)
#Zipp all candidate into a tuples
zipped_data = zip(candidates, candidate_perc, candidate_total)
#for loop
for row in zipped_data:
    print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) + ")")
    summary = (row[0] + ": ", str(row[1]) + "%", " (" + str(row[2]) + ")")
    summaries.append(summary)
for k in range(len(candidate_perc)):
    if candidate_total[k] > candidate_total[k - 1]:
        WinnerVotes = candidates[k]

#print results
print("----------------------------")
print("Winner:", WinnerVotes)
print("----------------------------")


#set the text output path
txt_output_path = os.path.join ("..", "Solved", "output_file")

# Open the file using "write" mode. Specify the variable to hold the contents
txt = open(txt_output_path, "w")

#write output file
txt.write("text\n")

txt.write("Election Results\n")
txt.write("---------------------------\n")
txt.write("Total Votes: " + str(num_rows) + "\n")
txt.write("---------------------------\n")

#need to bring this down here again to make it easier to write text file
for j in range(len(candidates)):
    candidate_count = 0
    for k in range(len(sorted_candidates)):
        if candidates[j] == sorted_candidates[k]:
            candidate_count += 1
    candidate_perc.append(round(candidate_count / num_rows * 100, 3))
    candidate_total.append(candidate_count)
zipped_data = zip(candidates, candidate_perc, candidate_total)
for row in zipped_data:

	txt.write(row[0] + (": ") + str(row[1]) + ("%") + "(" + str(row[2]) + ")\n")
txt.write("----------------------------\n")
txt.write("Winner: " + (WinnerVotes)+"\n")
txt.write("----------------------------\n")

#Completed



















































































