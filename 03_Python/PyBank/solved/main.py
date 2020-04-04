import os
import csv
# set the path for file
budget_csv = "../Resources/budget_data.csv"

# open the CSV
with open(budget_csv) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	next(csvreader)
	#set variables
	month_count = []
	PL_sum= []
	PL = []
	difference = []
	average_change = []
	greatest_increase = []
	greatest_decrease = []

#the total number of months in the dataset
#loop through looking for dataset
	for row in csvreader:
		month_count.append(row[0])
	#the sum of the profit and loss in the dataset
		PL.append(int(row[1]))
		PL_sum = sum(PL)
		#print outputs
	print("\ntext")
	print("\nFinancial Analysis")	
	print("---------------------------")
	print("Total Months: ", len(month_count))
	print("Total: $", PL_sum)

#loop through looking fro the difference in profit and loss
	for i in range(1, len(PL)):
		difference.append(PL[i] - PL[i-1])

#calculate the average difference of profit and loss 	
	average_change = sum(difference) / len(month_count)

	print("Average Change: $", round(average_change, 2))

#the greatest increase and decrease in profit and loss
	greatest_increase = max(difference)
	greatest_decrease = min(difference)
	greatest_max_date = str(month_count[difference.index(max(difference))])
	greatest_min_date = str(month_count[difference.index(min(difference))])
	#print outputs
	print("Greatest Increase in profits: ", greatest_max_date, "($" + str(greatest_increase),")")
	print("Greatest Increase in profits: ", greatest_min_date, "($" + str(greatest_decrease),")")


#set the text output path
txt_output_path = os.path.join ("..", "Solved", "output_file")

# Open the file using "write" mode. Specify the variable to hold the contents
txt = open(txt_output_path, "w")

#write output file
txt.write("text\n")

txt.write("Financial Analysis\n")
txt.write("---------------------------\n")
txt.write("Total Months: " +  str(len(month_count)) + "\n")
txt.write("Total: $" + str(PL_sum) + "\n")
txt.write("Average Change: $" + str(round(average_change, 2)) + "\n")
txt.write("Greatest Increase in profits: " +  str(greatest_max_date) + "($" + str(greatest_increase)+")" + "\n")
txt.write("Greatest Increase in profits: " +  str(greatest_min_date) +  "($" + str(greatest_decrease)+")" + "\n")

#Completed


    