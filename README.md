# python-challenge

This repo contains two folders - **PyBank** and **PyPoll**. Each folder contains a Python file with script that reads in a csv file from the **Resources** subfolder, performs analysis steps on the data, and prints the results to the terminal and to a text file in the **analysis** subfolder.

## PyBank
The PyBank csv is a financial dataset with "date" and "profit/loss" columns. The Python script iterates through the data to calculate:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

## PyPoll
The PyPoll csv contains fictitious election data. The Python script iterates through the data to calculate:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote
