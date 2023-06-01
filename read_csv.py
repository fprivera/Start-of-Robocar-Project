import csv 

with open("./donkey_path_old.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)
