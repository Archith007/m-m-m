import csv

with open("(H&W)eight.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    weights = file_data[i][2]
    new_data.append(float(weights))

length = len(new_data)
new_data.sort()

if length % 2 == 0:
    mid1 = int(length/2)
    mid2 = int(length/2 - 1)

    median = (new_data[mid1]+new_data[mid2])/2

else:
    mid = length / 2 
    median = new_data[mid]

print(median)
