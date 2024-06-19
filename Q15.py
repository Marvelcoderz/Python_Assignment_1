import csv
with open('C:/Users/sudhi/OneDrive/Desktop/New folder/demo.txt', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)