#Import modules
import os
import csv

#Specify file path
csvpath = os.path.join("Resources","election_data.csv")

#Create lists to store data
total_votes = 0
candidates = []
candidate_votes = [0,0,0]

#read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    #define the header first row
    csv_header = next(csvreader)
    
    #create a for loop to add data to lists
    #count total votes
    for row in csvreader:
        total_votes = total_votes + 1
        
        #find unique candidates and append to list
        if row[2] not in candidates:
            candidates.append(row[2])
        
        #count votes for each candidate
        for i in range(len(candidates)):
            if row[2] == candidates[i]:
                candidate_votes[i] = candidate_votes[i] + 1
            
    
#calculate percentage of votes for each candidate    
candidate_1_percentage = round((candidate_votes[0] / total_votes) * 100,3)
candidate_2_percentage = round((candidate_votes[1] / total_votes) * 100,3)
candidate_3_percentage = round((candidate_votes[2] / total_votes) * 100,3)

#Use index and max to identify winner name based on vote count
winner = candidates[candidate_votes.index(max(candidate_votes))]

#print to text file
print("Election Results")
print("---------------------------------------------------")
print(f"Total Votes: {(total_votes)}")
print("---------------------------------------------------")
print(f"{candidates[0]}: {candidate_1_percentage}% ({candidate_votes[0]})")
print(f"{candidates[1]}: {candidate_2_percentage}% ({candidate_votes[1]})")
print(f"{candidates[2]}: {candidate_3_percentage}% ({candidate_votes[2]})")
print("---------------------------------------------------")
print(f"Winner: {winner}")
print("---------------------------------------------------")

#Export a text file
#Specify the file path
output_path = os.path.join(".","analysis","PyPoll.txt")

#Open the file in write mode. Specify varialble to hold contents
with open(output_path, 'w') as txtfile:

    #print to text file
    print("Election Results",file=txtfile)
    print("---------------------------------------------------",file=txtfile)
    print(f"Total Votes: {(total_votes)}",file=txtfile)
    print("---------------------------------------------------",file=txtfile)
    print(f"{candidates[0]}: {candidate_1_percentage}% ({candidate_votes[0]})",file=txtfile)
    print(f"{candidates[1]}: {candidate_2_percentage}% ({candidate_votes[1]})",file=txtfile)
    print(f"{candidates[2]}: {candidate_3_percentage}% ({candidate_votes[2]})",file=txtfile)
    print("---------------------------------------------------",file=txtfile)
    print(f"Winner: {winner}",file=txtfile)
    print("---------------------------------------------------",file=txtfile)