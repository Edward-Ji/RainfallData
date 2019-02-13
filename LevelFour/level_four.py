import csv


# load from csv files
def load(file_name):
    with open(file_name, newline='') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        yield from reader


data = []
count = 1
lowest = 999
highest = 0

# manipulate
print("Day\t Rainfall")
for line in load("data.csv"):
    print(count, "\t", line[0])
    rain = int(line[0])
    data.append(rain)
    count += 1
    if rain < lowest:
        lowest = rain
    elif rain > highest:
        highest = rain

# output
print("Lowest:", lowest)
print("Highest:", highest)
print("Average:", round(sum(data) / count))
