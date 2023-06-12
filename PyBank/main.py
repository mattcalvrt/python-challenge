#modules
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#open the file using CSV module
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter =',')

    print(csvreader)

    #read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #set initial value for month count
    month_count = 0
    
    #read each row of data after the header
    for row in csvreader:
        print(row)

        #count months
        month_count = month_count + 1
        
    #print month_count after data rows    
    print("Total Months: " + str(month_count))

        






