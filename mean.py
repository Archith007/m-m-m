import csv

with open("(H&W)eight.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    weights = file_data[i][2]
    new_data.append(float(weights))
total = 0
for i in new_data:
    total = total + i

n = len(new_data)
mean = total/n

print("Mean is : ", mean)