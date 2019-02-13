# one-liner
print("Input data below\nDay       Rainfall") or print("Rainfall that day: " + [input(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][day].ljust(10, ' ') + "") for day in range(0, 7)][["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(input("Choose a day: "))])
