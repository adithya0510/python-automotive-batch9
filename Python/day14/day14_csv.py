import csv

filename = "test.csv"
fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

fields = next(csvreader)  # read the objects
for row in csvreader:  #read the rows
    rows.append(row)