import csv

with open('class2.csv',newline='') as f:
    reader = csv.reader(f)
    file_data=list(reader)


#To remove header from CSV

file_data.pop(0)

total_marks = 0
total_entries = len(file_data)

for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks/total_entries
print ("Mean (Average) is ->"+str(mean))