
import csv
from collections import Counter

with open("(H&W)eight.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    weights = file_data[i][2]
    new_data.append(float(weights))

data = Counter(new_data)

mode_data_for_range = {
    "75-85":0,
    "85-95" : 0,
    "95-105":0,
    "105-115" : 0,
    "115-125" : 0,
    "125-135" : 0,
    "135-145" : 0,
    "145-155" : 0,
    "155-165" : 0,
    "165-175" : 0
}

for weight,occurance in data.items():
    if 75<float(weight) <85:
        mode_data_for_range["75-85"] +=occurance
    elif 85<float(weight)<95:
        mode_data_for_range["85-95"] +=occurance
    elif 95<float(weight)<105:
        mode_data_for_range["95-105"] +=occurance
    elif 105<float(weight)<115:
        mode_data_for_range["105-115"] +=occurance
    elif 115<float(weight)<125:
        mode_data_for_range["115-125"] +=occurance
    elif 125<float(weight)<135:
        mode_data_for_range["125-135"] +=occurance
    elif 135<float(weight)<145:
        mode_data_for_range["135-145"] +=occurance
    elif 145<float(weight)<155:
        mode_data_for_range["145-155"] +=occurance
    elif 155<float(weight)<165:
        mode_data_for_range["155-165"] +=occurance
    else:
        mode_data_for_range["165-175"] +=occurance

        
print(mode_data_for_range)
mode_range, mode_occurence = 0, 0

for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is : {mode:2f}")