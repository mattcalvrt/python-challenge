#Import modules
import os
import csv

#Specify the file path
csvpath = os.path.join('Resources', 'budget_data.csv')

#Create lists to store data
date = []
profit = []
profit_change = []

#Read the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Define the header first row
    csv_header = next(csvreader)

    # Create a for loop to add data to lists
    for row in csvreader:
        date.append(row[0])
        profit.append(int(row[1]))

    #Create for loop for profit change
    for i in range(1,len(profit)):
        profit_change.append(profit[i]-profit[i-1])

    #Calculate average, max, and minimum profit change
    avg_profit_change = round(sum(profit_change)/(len(profit_change)),2)
    max_profit_change = max(profit_change)
    min_profit_change = min(profit_change)

    #find date of max and min revenue change
    max_profit_change_date = str(date[profit_change.index(max_profit_change)+1])
    min_profit_change_date = str(date[profit_change.index(min_profit_change)+1])

#Print to terminal
print("Financial Analysis")
print("---------------------------------------------------")
print("Total Months: " + str(len(date)))
print("Total: $" + str(sum(profit)))
print(f"Average Change: ${str(avg_profit_change)}")
print(f"Greatest Increase in Profits: {max_profit_change_date} (${str(max_profit_change)})")
print(f"Greatest Decrease in Profits: {min_profit_change_date} (${str(min_profit_change)})")

#Export a text file
#Specify the file path
output_path = os.path.join(".","analysis","PyBank.txt")

#Open the file in write mode. Specify varialble to hold contents
with open(output_path, 'w') as txtfile:

    #print to text file
    print("Financial Analysis", file=txtfile)
    print("---------------------------------------------------", file=txtfile)
    print("Total Months: " + str(len(date)), file=txtfile)
    print("Total: $" + str(sum(profit)), file=txtfile)
    print(f"Average Change: ${str(avg_profit_change)}", file=txtfile)
    print(f"Greatest Increase in Profits: {max_profit_change_date} (${str(max_profit_change)})", file=txtfile)
    print(f"Greatest Decrease in Profits: {min_profit_change_date} (${str(min_profit_change)})", file=txtfile)