week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Input data below")
print("Day       Rainfall")
rain = [int(input(day.ljust(10, ' '))) for day in week]

# calculate average
print("Average rainfall of the week:", round(sum(rain) / len(rain)))

day = input("Choose a day from the week: ")
if day.title() not in week:
    print(day, "is not in the week!")
else:
    print("Rainfall on", day + ':', rain[week.index(day)])